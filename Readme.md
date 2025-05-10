# TraceKashef

**TraceKashef** is a modern, web-based trace visualization tool for embedded developers working with RTOS environments. It decodes trace files in the [Percepio](https://percepio.com) PSF format and displays them in real time using a multi-client architecture built on WebAssembly and [Perspective](https://github.com/finos/perspective).

---

## 🔍 Features

- ✅ Full support for FreeRTOS PSF event decoding
- ✅ Multi-client live viewing (WebSocket-based)
- ✅ WebAssembly-powered frontend with [Perspective Viewer](https://perspective.finos.org/)
- ✅ Built-in trace streamer and decoder
- ✅ Real-time and post-mortem trace analysis
- ✅ Python and JavaScript hybrid architecture

---

## 🚀 Demo

> Coming soon!  
Add screenshots or screen recordings here.

---

## 📦 Tech Stack

- **Backend**: Python, Tornado, PyArrow
- **Frontend**: Perspective.js
- **Protocol**: WebSocket (server-client for streaming trace updates)

---

## 🛠 Usage

### 1. Clone the repo

```bash
git clone https://github.com/The-Sent-Horses/TraceKashef.git
cd TraceKashef
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
pnpm install
``` 

### 3. choose a trace file
in the server.py file, at line 36: set the path to your trace file.  

### 4. Run the server

```bash
pnpm run start
```

### 5. Open the web interface
Open your web browser and navigate to `http://localhost:8080` to access the TraceKashef web interface.