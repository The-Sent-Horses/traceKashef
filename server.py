import os
import logging
import tornado.web
import tornado.ioloop


import perspective
import perspective.handlers.tornado


from streamer import Streamer
from decoder import psf_reader

import pyarrow as pa
import pyarrow.ipc as ipc


schema_dict = {
    "timestamp": "string",
    "event_type": "string",
    "pointer": "string",
    "value": "string",
    "name": "string",
    "handle_1": "string",
    "handle_2": "string",
    "arg1": "string",
    "arg2": "string",
    "arg3": "string",
    "arg4": "string",
    "func_hash": "string",
    "mem_usage": "string",
}





def perspective_thread(perspective_server,
                       psf_path= "/mnt/c/Program Files/Percepio/Tracealyzer 4/FreeRTOS/demo_freertos.psf",
                       arrow_out="snapshot.arrow",
                       ):
    
    client = perspective_server.new_local_client()
    
    trace = psf_reader.psf_reader(psf_path)
    trace.get_header()
    trace.skip_white_space()
    table = client.table(schema_dict, name="freertos_table")
    streamer = Streamer(traceKashef=trace, perspective_table=table)
    
    # update with new data every 50ms
    def convert_psf_to_arrow():
        tables = []
        while True:
            batch = streamer.create_batch_array()
            if batch == 0:
                continue
            if batch == -1:
                break
            tables.append(batch)
            print(".", end = "")
        if tables:
            combined = pa.concat_tables(tables)
            with pa.OSFile(arrow_out, "wb") as sink:
                writer = ipc.new_file(sink, combined.schema)
                writer.write_table(combined)
                writer.close()  
       

    convert_psf_to_arrow()
    
    with pa.memory_map(arrow_out, "r") as source:
        table = ipc.open_file(source).read_all()
    
    perspective_table = client.table(table, name="freertos_table")
    

def make_app(perspective_server):
    return tornado.web.Application(
        [
            (
                r"/websocket",
                perspective.handlers.tornado.PerspectiveTornadoHandler,
                {"perspective_server": perspective_server},
            ),
            (
                r"/node_modules/(.*)",
                tornado.web.StaticFileHandler,
                {"path": "./node_modules/"},
            ),
            (
                r"/(.*)",
                tornado.web.StaticFileHandler,
                {"path": "./", "default_filename": "index.html"},
            ),
        ]
    )




if __name__ == "__main__":
    perspective_server = perspective.Server()

    app = make_app(perspective_server)
    app.listen(8080)
    logging.critical("Listening on http://localhost:8080")
    loop = tornado.ioloop.IOLoop.current()
    loop.call_later(0, perspective_thread, perspective_server)
    loop.start()
    
