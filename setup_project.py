
import os
import json
from pathlib import Path

def create_directory_structure():
    # Define the directory structure
    directories = [
        "data/raw",
        "data/interim",
        "data/processed",
        "notebooks",
        "src/data",
        "src/api",
        "src/utils",
        "tests",
        "docs"
    ]
    
    # Create directories
    for dir_path in directories:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        # Create __init__.py in Python package directories
        if dir_path.startswith('src'):
            (Path(dir_path) / '__init__.py').touch()

def create_config_template():
    config = {
        "credentials": {
            "snac_api": {
                "base_url": "https://api.snaccooperative.org/"
            },
            "archivesspace_api": {
                "api_url": "https://testarchivesspace.library.yale.edu/api",
                "username": "",
                "password": ""
            }
        },
        "settings": {
            "csv_encoding": "utf-8",
            "batch_size": 100
        }
    }
    
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

def create_gitignore():
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/

# Jupyter Notebook
.ipynb_checkpoints

# VS Code
.vscode/

# Credentials
config.json

# Data
data/raw/*
data/interim/*
data/processed/*
!data/raw/.gitkeep
!data/interim/.gitkeep
!data/processed/.gitkeep
"""
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)

def create_readme():
    readme_content = """# ArchivesSpace SNAC Enrichment

A project to enrich ArchivesSpace agent records with SNAC identifiers and manage authority data.

## Project Structure
- `data/`: CSV and processed data files
- `notebooks/`: Jupyter notebooks for analysis and reports
- `src/`: Source code
- `docs/`: Documentation

## Setup
1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment: `venv\\Scripts\\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `config.json` template and update with your credentials

## Usage
[Add usage instructions here]
"""
    with open('README.md', 'w') as f:
        f.write(readme_content)

def create_requirements():
    requirements = [
        "jupyterlab",
        "pandas",
        "requests",
        "numpy",
        "python-dotenv",
        "openpyxl",  # for Excel support
        "pytest"     # for testing
    ]
    
    with open('requirements.txt', 'w') as f:
        f.write('\n'.join(requirements))

def create_initial_notebook():
    notebook_content = """# Initial Data Exploration
This notebook will be used for processing my thoughts, as I explore, clean up, and enrich the ArchivesSpace agent data.

## Setup
```python
import pandas as pd
import json
import requests
from pathlib import Path

Load Configuration

with open('../config.json') as f:
    config = json.load(f)
    
    Load and Examine Data
[Add data loading and examination code here]
"""
    notebook_path = Path('notebooks/01_initial_exploration.md')
    notebook_path.write_text(notebook_content)

def main():
    print("Setting up project structure...")
    create_directory_structure()
    create_config_template()
    create_gitignore()
    create_readme()
    create_requirements()
    create_initial_notebook()
    print("Project setup complete!")

if __name__ == "__main__":
    main()
