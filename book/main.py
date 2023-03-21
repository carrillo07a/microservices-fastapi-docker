from fastapi import FastAPI
import socket

app = FastAPI()


@app.get("/book")
async def root():
    return {"message": f"Book API Container ID: {socket.gethostname()}"}
