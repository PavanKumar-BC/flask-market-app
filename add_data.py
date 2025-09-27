from market import db, app
from market.models import Item

with app.app_context():
    # Create some items

    item4 = Item(name="phone", price=100, barcode="456889123456", description="ok")
    item5 = Item(name="kiran", price=100, barcode="456889144456", description="okk")


    # Add to database

    db.session.add(item4)
    db.session.add(item5)


    db.session.commit()
    print("Items added successfully!")
