from fastapi import FastAPI
import subprocess
import os

from constants import ALLOWED_BRANCH_NAMES

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "ok"}


@app.post("/update/{branch_name}")
async def update_branch(branch_name: str):
  if branch_name not in ALLOWED_BRANCH_NAMES:
      return {"success": False, "errors": [{"error": "Branch name not allowed!"}]}

  os.environ["BRANCH_NAME"] = branch_name
  subprocess.call(["sh", "./release-bot.sh"])

  return {"success": True}
