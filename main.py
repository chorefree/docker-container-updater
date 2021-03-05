from fastapi import FastAPI
import subprocess
import os
import uvicorn

import settings
from constants import ALLOWED_CONTAINER_NAMES

app = FastAPI()
dir_path = os.path.dirname(os.path.realpath(__file__))


@app.get("/")
async def root():
    return {"message": "ok"}


@app.post("/restart/{container_name}")
async def restart_container(container_name: str):
    if container_name not in ALLOWED_CONTAINER_NAMES:
        return {"success": False, "errors": [{"error": "Container name not allowed!"}]}

    os.environ["CONTAINER_NAME"] = container_name
    subprocess.call(["sh", dir_path + "/restart-container.sh"])

    return {"success": True}


@app.post("/update/{container_name}")
async def update_container(container_name: str):
    if container_name not in ALLOWED_CONTAINER_NAMES:
        return {"success": False, "errors": [{"error": "Container name not allowed!"}]}

    os.environ["CONTAINER_NAME"] = container_name
    os.environ["ECR_REPO"] = container_name.replace("_", "-")
    subprocess.call(["sh", dir_path + "/release-container.sh"])

    return {"success": True}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000)
