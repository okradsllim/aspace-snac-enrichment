# -*- coding: utf-8 -*-
import json
from pathlib import Path

def create_directory_structure():
    directories = [
        "notebooks",
        "src/data",
        "src/api"
    ]
    
    for dir_path in directories:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
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
    
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)

def create_gitignore():
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/

# VS Code
.vscode/

# Credentials
config.json

# ArchivesSpace Cache
src/data/aspace_cache/

# Notebook checkpoints
.ipynb_checkpoints
"""
    with open('.gitignore', 'w', encoding='utf-8') as f:
        f.write(gitignore_content)

def create_readme():
    readme_content = """# ArchivesSpace SNAC Enrichment

A project to enrich ArchivesSpace agent records with SNAC identifiers and manage authority data.

## Project Structure
- `notebooks/`: Placeholder for optional notebooks.
- `src/`: Source code for data handling and API queries.
- `config.json`: Stores credentials and settings.

## Setup
1. Clone the repository.
2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   **Windows:**
   ```bash
   venv\\Scripts\\activate
   ```

   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Copy or modify `config.json` to include your ArchivesSpace and SNAC credentials.

## Usage
[Add usage instructions here, depending on your scripts in `src/api` and `src/data`.]
"""

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

def create_requirements():
    requirements = [
        "pandas",
        "requests",
        "numpy",
        "python-dotenv",
        "openpyxl"
    ]
    
    with open('requirements.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(requirements) + "\n")

def main():
    print("Setting up project structure...")
    
    create_directory_structure()
    create_config_template()
    create_gitignore()
    create_readme()
    create_requirements()
    
    print("Project setup complete!")

if __name__ == "__main__":
    main()
