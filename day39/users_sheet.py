from data_manager import DataManager

while True:
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email_id = input("Enter your email address: ")
    dm = DataManager(id=None, city=None, iata_code=None, lowest_price=None, first_name=first_name, last_name=last_name, email_id=email_id)
    dm.add_user()