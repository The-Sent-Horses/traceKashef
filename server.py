import os
import logging
import tornado.web
import tornado.ioloop


import perspective
import perspective.handlers.tornado


from streamer import Streamer
from decoder import psf_reader



schema_dict = {
    "timestamp": "integer",
    "event_type": "string",
    "pointer": "integer",
    "value": "integer",
    "name": "string",
    "handle_1": "integer",
    "handle_2": "integer",
    "arg1": "string",
    "arg2": "string",
    "arg3": "string",
    "arg4": "string",
    "func_hash": "integer",
}

    
    
def perspective_thread(perspective_server):
    client = perspective_server.new_local_client()
    
    psf_path = "/mnt/c/Program Files/Percepio/Tracealyzer 4/FreeRTOS/demo_freertos.psf"
    trace = psf_reader.psf_reader(psf_path)
    trace.get_header()
    trace.skip_white_space()
    table = client.table(schema_dict, name="freertos_table")
    streamer = Streamer(traceKashef=trace, perspective_table=table)
    
    # update with new data every 50ms
    def updater():
        data = streamer.create_batch_array()
        if data:
            table.update(data)
       

    callback = tornado.ioloop.PeriodicCallback(callback=updater, callback_time=0.01)
    callback.start()
    

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
    
