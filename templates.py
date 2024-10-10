import os

def create_project_structure():
    # Define the project structure
    project_structure = {
        'app': [
            '__init__.py',
            'rss_parser.py',
            'database.py',
            'tasks.py',
            'classifier.py',
            'models.py'
        ],
        'logs': [
            'app.log'
        ],
        'tests': [
            'test_app.py'
        ],
        'config': [
            'config.yaml'
        ],
        'venv': [],
        'requirements.txt': [],
        'README.md': [],
        'run_celery.sh': []
    }

    # Create the project structure
    for folder, files in project_structure.items():
        if files:  # If there are files in the folder
            os.makedirs(folder, exist_ok=True)  # Create the folder
            for file in files:
                open(os.path.join(folder, file), 'w').close()  # Create each file
        else:
            os.makedirs(folder, exist_ok=True)  # Create empty folders

    print("Project structure created successfully.")

if __name__ == "__main__":
    create_project_structure()
