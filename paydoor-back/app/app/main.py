from fastapi import FastAPI
from fastapi.responses import Response


app = FastAPI()


@app.post("/")
async def add_email():
    return Response(status_code=200)