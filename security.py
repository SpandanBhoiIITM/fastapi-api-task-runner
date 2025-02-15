from pathlib import Path
from fastapi import HTTPException

DATA_DIR = Path("data").resolve()

def enforce_data_restrictions(file_path: Path):
    """Ensure file operations are restricted to the /data directory."""
    if not file_path.resolve().is_relative_to(DATA_DIR):
        raise HTTPException(status_code=403, detail="Access outside /data is forbidden.")

def prevent_deletion():
    """Prevent deletion of any file."""
    raise HTTPException(status_code=403, detail="File deletion is forbidden.")
