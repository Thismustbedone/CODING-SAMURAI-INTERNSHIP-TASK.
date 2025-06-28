import os

# Folder structure
folders = [
    "personal_blog/static",
    "personal_blog/templates"
]

# File structure with initial content
files = {
    "personal_blog/app.py": "",
    "personal_blog/models.py": "",
    "personal_blog/forms.py": "",
    "personal_blog/blog.db": "",  # this will be auto-created by SQLAlchemy
    "personal_blog/static/style.css": "body { font-family: Arial; background-color: #f4f4f4; }",
    "personal_blog/templates/base.html": "",
    "personal_blog/templates/home.html": "",
    "personal_blog/templates/login.html": "",
    "personal_blog/templates/register.html": "",
    "personal_blog/templates/dashboard.html": "",
    "personal_blog/templates/create_post.html": "",
    "personal_blog/templates/edit_post.html": "",
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(file_path, 'w') as file:
        file.write(content)

print("Flask blog project structure created successfully!")
