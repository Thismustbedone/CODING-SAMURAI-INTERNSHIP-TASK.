from app import app, db
from models import Post
from datetime import datetime

# Create posts
with app.app_context():
    post1 = Post(
        title="Welcome to My Blog",
        content="This is my first post on the blog. I'll share my coding experiences and tutorials here.",
        date=datetime.utcnow(),
        user_id=1
    )
    post2 = Post(
        title="Getting Started with Flask",
        content="Flask is a lightweight and easy-to-use Python web framework. It’s perfect for beginners.",
        date=datetime.utcnow(),
        user_id=1
    )
    post3 = Post(
        title="How This Blog Was Built",
        content="I built this blog using Flask, SQLAlchemy, Jinja2 templates, and a lot of coffee ☕.",
        date=datetime.utcnow(),
        user_id=1
    )

    db.session.add_all([post1, post2, post3])
    db.session.commit()
    print("✅ Sample blog posts added successfully!")
