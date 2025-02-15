from fastapi import FastAPI, HTTPException
from pathlib import Path
import shutil

app = FastAPI()

# Define data directory
DATA_DIR = Path("data")  # Relative path, assuming data/ exists in the project root
DATA_DIR.mkdir(exist_ok=True)  # Ensure directory exists

@app.get("/")
def home():
    return {"message": "FastAPI File Manager is running!"}

# ✅ 1. List all files in `/data/`
@app.get("/list-files")
def list_files():
    files = [f.name for f in DATA_DIR.iterdir() if f.is_file()]
    return {"files": files}

# ✅ 2. Read a file from `/data/`
@app.get("/read-file/{filename}")
def read_file(filename: str):
    file_path = DATA_DIR / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail=f"File not found: {filename}")
    
    with file_path.open("r", encoding="utf-8") as file:
        content = file.read()
    
    return {"filename": filename, "content": content}

# ✅ 3. Write to a file in `/data/`
@app.post("/write-file/{filename}")
def write_file(filename: str, content: str):
    file_path = DATA_DIR / filename
    with file_path.open("w", encoding="utf-8") as file:
        file.write(content)
    return {"message": f"File '{filename}' written successfully."}

# ✅ 4. Append to an existing file in `/data/`
@app.post("/append-file/{filename}")
def append_file(filename: str, content: str):
    file_path = DATA_DIR / filename
    with file_path.open("a", encoding="utf-8") as file:
        file.write(content)
    return {"message": f"Content appended to '{filename}'."}

# ✅ 5. Copy a file within `/data/`
@app.post("/copy-file/{filename}/{new_filename}")
def copy_file(filename: str, new_filename: str):
    src = DATA_DIR / filename
    dest = DATA_DIR / new_filename
    if not src.exists():
        raise HTTPException(status_code=404, detail=f"File not found: {filename}")
    shutil.copy(src, dest)
    return {"message": f"File '{filename}' copied to '{new_filename}'."}

# ✅ 6. Move a file within `/data/`
@app.post("/move-file/{filename}/{new_filename}")
def move_file(filename: str, new_filename: str):
    src = DATA_DIR / filename
    dest = DATA_DIR / new_filename
    if not src.exists():
        raise HTTPException(status_code=404, detail=f"File not found: {filename}")
    shutil.move(str(src), str(dest))
    return {"message": f"File '{filename}' moved to '{new_filename}'."}

# ✅ 7. Rename a file within `/data/`
@app.post("/rename-file/{old_filename}/{new_filename}")
def rename_file(old_filename: str, new_filename: str):
    old_path = DATA_DIR / old_filename
    new_path = DATA_DIR / new_filename
    if not old_path.exists():
        raise HTTPException(status_code=404, detail=f"File not found: {old_filename}")
    old_path.rename(new_path)
    return {"message": f"File '{old_filename}' renamed to '{new_filename}'."}

# ✅ 8. Create a new empty file in `/data/`
@app.post("/create-file/{filename}")
def create_file(filename: str):
    file_path = DATA_DIR / filename
    file_path.touch(exist_ok=True)
    return {"message": f"File '{filename}' created."}

# ✅ 9. Create a new directory in `/data/`
@app.post("/create-dir/{dirname}")
def create_directory(dirname: str):
    dir_path = DATA_DIR / dirname
    dir_path.mkdir(exist_ok=True)
    return {"message": f"Directory '{dirname}' created."}

# ✅ 10. List subdirectories in `/data/`
@app.get("/list-dirs")
def list_dirs():
    dirs = [d.name for d in DATA_DIR.iterdir() if d.is_dir()]
    return {"directories": dirs}
