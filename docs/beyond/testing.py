from fastapi import FastAPI, HTTPException, Query
import os
import requests
import sqlite3
import shutil
from git import Repo
import markdown
import pandas as pd
from pydantic import BaseModel
from pathlib import Path

app = FastAPI()

DATA_DIR = Path("/data")

# Security check to ensure paths stay within /data/
def secure_path(file_path: str) -> Path:
    path = DATA_DIR / Path(file_path).name
    if not path.resolve().is_relative_to(DATA_DIR):
        raise HTTPException(status_code=400, detail="Access outside /data/ is not allowed.")
    return path

@app.post("/run")
def run_task(task: str):
    if "fetch data from" in task.lower():
        return fetch_api_data()
    elif "clone repo" in task.lower():
        return clone_git_repo()
    elif "run sql query" in task.lower():
        return run_sql_query()
    elif "extract data from website" in task.lower():
        return extract_website_data()
    elif "resize image" in task.lower():
        return process_image()
    elif "transcribe audio" in task.lower():
        return transcribe_audio()
    elif "convert markdown" in task.lower():
        return convert_markdown()
    elif "filter csv" in task.lower():
        return filter_csv()
    else:
        raise HTTPException(status_code=400, detail="Unknown task.")

@app.get("/read")
def read_file(path: str):
    file_path = secure_path(path)
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found.")
    return file_path.read_text()

# Task B3: Fetch API Data
def fetch_api_data():
    url = "https://api.publicapis.org/entries"
    response = requests.get(url)
    if response.status_code == 200:
        file_path = secure_path("api_data.json")
        file_path.write_text(response.text)
        return {"message": "API data fetched and saved.", "file": str(file_path)}
    else:
        raise HTTPException(status_code=500, detail="Failed to fetch API data.")

# Task B4: Clone Git Repository
def clone_git_repo():
    repo_url = "https://github.com/example/example-repo.git"
    repo_path = secure_path("repo")
    Repo.clone_from(repo_url, repo_path)
    return {"message": "Git repo cloned.", "repo": str(repo_path)}

# Task B5: Run SQL Query
def run_sql_query():
    db_path = secure_path("ticket-sales.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(price * units) FROM tickets WHERE type = 'Gold'")
    total_sales = cursor.fetchone()[0]
    conn.close()
    file_path = secure_path("ticket-sales-gold.txt")
    file_path.write_text(str(total_sales))
    return {"message": "SQL query executed.", "total_sales": total_sales}

# Additional functions for B6-B10 will be added next...
