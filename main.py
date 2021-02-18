from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "ok"}

@app.post("/update/{branch_name}")
async def update_branch(branch_name: str):

  os.environ["BRANCH_NAME"] = branch_name
  subprocess.call(["sh", "./release-bot.sh"])

  return {"success": True}

