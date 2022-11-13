import sys, os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s]: %(message)s"
)

while True:

    project_name = input("Enter the Project Name :")
    if project_name != '':
        break

logging.info(f"Creating Project by name : {project_name}")

#list of files

list_of_files = [
    ".github/workflows/.gitkeep",
    f"{project_name}/__init__.py",
    "__init__.py",
    "setup.py",
    "requirements.txt",
    "requirements-dev.txt",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini",
    "init_setup.sh",
    "main.py"
]

for filepath in list_of_files:
    filedir, filename = os.path.split(Path(filepath))
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory at {filedir} for file : {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a new file : {filename} at file path {filepath}")
    
    else:
        logging.info(f"file is already present at {filepath}")
