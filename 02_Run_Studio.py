import os
import subprocess

print("🎬 Starting AI Animation Studio")

PROJECT_PATH = "/content/AI-Animation-Studio"

if not os.path.exists(PROJECT_PATH):
    print("Downloading project...")
    subprocess.run([
        "git",
        "clone",
        "https://github.com/saeedhomayoun27-cmd/AI-Animation-Studio.git",
        PROJECT_PATH
    ])

os.chdir(PROJECT_PATH)

print("Project loaded successfully")

subprocess.run([
    "python",
    "launch.py"
])
