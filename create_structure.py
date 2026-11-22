
from pathlib import Path

# Project folders
folders = [
    "src/enterprisegraderag",
    "src/enterprisegraderag/templates",
    "src/enterprisegraderag/static/css",
    "src/enterprisegraderag/static/js",
    "worker",
    "infra",
    "scripts",
    "docs",
    "tests",
]

# Project files
files = [
    # Root files
    ".env",
    ".env.example",
    ".gitignore",
    "README.md",

    # Backend
    "src/enterprisegraderag/__init__.py",
    "src/enterprisegraderag/main.py",
    "src/enterprisegraderag/config.py",
    "src/enterprisegraderag/db.py",
    "src/enterprisegraderag/aws.py",
    "src/enterprisegraderag/vector.py",
    "src/enterprisegraderag/rag.py",
    "src/enterprisegraderag/memory.py",
    "src/enterprisegraderag/guardrails.py",
    "src/enterprisegraderag/graph.py",
    "src/enterprisegraderag/observability.py",

    # Frontend
    "src/enterprisegraderag/templates/index.html",
    "src/enterprisegraderag/static/css/styles.css",
    "src/enterprisegraderag/static/js/app.js",

    # Document ingestion
    "worker/__init__.py",
    "worker/ingest.py",

    # Database
    "infra/schema.sql",
    "scripts/init_db.py",

    # Documentation
    "docs/SETUP.md",

    # Testing
    "tests/__init__.py",
]


def create_structure():

    for folder in folders:
        Path(folder).mkdir(
            parents=True,
            exist_ok=True
        )

    for file in files:
        path = Path(file)
        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )
        path.touch(exist_ok=True)

    print("Project structure created successfully!")
    print(f"Total folders: {len(folders)}")
    print(f"Total files: {len(files)}")


if __name__ == "__main__":
    create_structure()
