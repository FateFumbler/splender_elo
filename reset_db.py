from app import app
from models import db
from seed_test_data import seed_test_data

with app.app_context():
    print("Dropping all tables...")
    db.drop_all()
    print("Creating all tables...")
    db.create_all()
    print("Seeding test data...")
    seed_test_data()
    print("Done!")
