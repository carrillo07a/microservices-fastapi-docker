from fastapi import FastAPI
import socket

app = FastAPI()


@app.get("/blacklist")
async def root():
    return {"message": f"Blacklist API Container ID: {socket.gethostname()}"}
