import requests
import numpy as np
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World", "numpy_version": np.__version__}