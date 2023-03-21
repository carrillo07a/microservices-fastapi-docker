from fastapi import FastAPI
import socket

app = FastAPI()


@app.get("/blog")
async def root():
    return {"message": f"Blog API Container ID: {socket.gethostname()}"}
