FastAPI Task Runner 🚀
This is a FastAPI-based automation agent that processes tasks using an LLM (GPT-4o-Mini), interacts via API, and handles file processing. The API is containerized using Docker for easy deployment.

📌 Features
Runs automation tasks using FastAPI
Uses AI Proxy Token for authentication
Dockerized for easy deployment
API Endpoints to execute tasks and read files
🔧 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/spandanbhoi/fastapi-api-task-runner.git
cd fastapi-api-task-runner
2️⃣ Install Dependencies
bash
Copy
Edit
pip install fastapi uvicorn
3️⃣ Run the API Locally
bash
Copy
Edit
uvicorn app:app --host 0.0.0.0 --port 8000
🐳 Using Docker
1️⃣ Pull the Docker Image
bash
Copy
Edit
docker pull spandanbhoi/fastapi-api-task-runner
2️⃣ Run the Docker Container
bash
Copy
Edit
docker run -e AIPROXY_TOKEN=<your-token> -p 8000:8000 spandanbhoi/fastapi-api-task-runner
📌 API Endpoints
🔹 Run a Task
Request:

bash
Copy
Edit
POST /run?task=<task_name>
Example:

bash
Copy
Edit
curl -X POST "http://localhost:8000/run?task=example_task"
🔹 Read a File
Request:

bash
Copy
Edit
GET /read?path=<file_path>
Example:

bash
Copy
Edit
curl -X GET "http://localhost:8000/read?path=/app/data/output.txt"
📜 License
This project is licensed under the MIT License.
