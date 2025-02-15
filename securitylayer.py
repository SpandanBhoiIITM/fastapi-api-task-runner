import os
import re
import shutil
from fastapi import FastAPI, HTTPException

app = FastAPI()

DATA_DIR = "/data/"  # Restrict all file operations to this directory

def validate_path(file_path: str):
    """Ensure the requested path is inside /data/"""
    abs_path = os.path.abspath(file_path)
    if not abs_path.startswith(DATA_DIR):
        raise HTTPException(status_code=403, detail="Access to this path is restricted.")

def block_deletion(func):
    """Decorator to prevent file deletions"""
    def wrapper(*args, **kwargs):
        raise HTTPException(status_code=403, detail="File deletions are not allowed.")
    return wrapper

# Secure file operations
@app.get("/read")
def read_file(path: str):
    validate_path(path)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")
    
    with open(path, "r", encoding="utf-8") as f:
        return {"content": f.read()}

# Block any deletion attempt
os.remove = block_deletion(os.remove)
shutil.rmtree = block_deletion(shutil.rmtree)
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
