from market import db
from market import app

with app.app_context():
    db.create_all()
    print("Database created successfully!")
