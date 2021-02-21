from fastapi import FastAPI
import subprocess
import os
import uvicorn

from constants import ALLOWED_BRANCH_NAMES

app = FastAPI()
dir_path = os.path.dirname(os.path.realpath(__file__))

@app.get("/")
async def root():
    return {"message": "ok"}

@app.post("/update/{branch_name}")
async def update_branch(branch_name: str):
  if branch_name not in ALLOWED_BRANCH_NAMES:
      return {"success": False, "errors": [{"error": "Branch name not allowed!"}]}

  os.environ["BRANCH_NAME"] = branch_name
  print(dir_path)
  subprocess.call(["sh", dir_path + "/release-bot.sh"])

  return {"success": True}

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=5000)

