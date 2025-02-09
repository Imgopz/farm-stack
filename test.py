import os

folders = [
    "app",
    "app/auth",
    "app/database",
    "app/tasks",
    "app/llm",
    "app/observability",
    "app/parsers",
    "app/templates",
    "app/alembic",
    "app/tests",
    "scripts"
]

files = {
    "app/__init__.py": "",
    "app/main.py": "from fastapi import FastAPI\n\napp = FastAPI(title=\"FastAPI Backend\")\n\n@app.get('/')\ndef read_root():\n    return {\"message\": \"Welcome to FastAPI Backend\"}\n",
    "app/config.py": "from pydantic_settings import BaseSettings\n\nclass Settings(BaseSettings):\n    DATABASE_URL: str\n    SECRET_KEY: str\n    CELERY_BROKER_URL: str\n    CELERY_RESULT_BACKEND: str\n\n    class Config:\n        env_file = '.env'\n\nsettings = Settings()\n",
    "app/auth/__init__.py": "",
    "app/database/__init__.py": "",
    "app/tasks/__init__.py": "",
    "app/llm/__init__.py": "",
    "app/observability/__init__.py": "",
    "app/parsers/__init__.py": "",
    "app/templates/email_template.jinja": "Hello {{ user_name }},\n\nThis is a test email.\n",
    "app/alembic/__init__.py": "",
    "app/tests/__init__.py": "",
    "scripts/run_dev.sh": "#!/bin/bash\necho \"Starting Development Server\"\n",
    "scripts/run_prod.sh": "#!/bin/bash\necho \"Starting Production Server\"\n",
    "requirements.txt": "fastapi\nuvicorn\npydantic-settings\nsqlalchemy\ncelery\nredis\nlangchain\ninstructor\npymupdf\nfaiss-cpu\nopenai\n",
    ".env": "DATABASE_URL=postgresql://user:password@localhost/dbname\nSECRET_KEY=your_secret_key\nCELERY_BROKER_URL=redis://localhost:6379/0\nCELERY_RESULT_BACKEND=redis://localhost:6379/0\n",
    "README.md": "# FastAPI Backend\n\nA scalable FastAPI backend template with authentication, Celery, LLM integration, and observability."
}

def create_folders():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    print("✅ Folders created successfully.")

def create_files():
    for file_path, content in files.items():
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    print("✅ Files created successfully.")

def main():
    create_folders()
    create_files()
    print("🚀 Project structure is ready!")

if __name__ == "__main__":
    main()
