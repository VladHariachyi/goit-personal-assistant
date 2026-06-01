from collections import UserDict
from datetime import datetime, timedelta
from .record import Record
from ..shared import AddressBookError


class AddressBook(UserDict):
    """Dictionary-based address book storage."""
        
    def add_record(self, record: Record) -> None:
        name = record.name.value
        if self.find_record(name):
            raise AddressBookError("Contact already exists")
        self.data[name] = record

    def rename_record(self, old_name: str, new_name: str) -> None:
        real_key = next((key for key in self.data.keys() if key.strip().lower() == old_name.lower()), None)
        if not real_key:
            raise AddressBookError("Contact not found.")
        record = self.data.pop(real_key)
        self.data[new_name] = record


    def find_record(self, name: str) -> Record | None:
        for key, record in self.data.items():
            if key.strip().lower() == name.lower():
                return record
        return None
    
        
    def delete(self, name: str) -> None:
        record = self.find_record(name)
        if not record:
            raise AddressBookError("Contact not found.")
        self.data.pop(record.name.value)

    def get_upcoming_birthdays(self, requested_days: int) -> list:
        print("inside get_upcoming_birthdays")
        today = datetime.today().date()
        delta_date = today + timedelta(days = requested_days)
        congratulations_list = []
    
        for name, record in self.data.items():
            if record.birthday is None:
                continue

            birthday = record.birthday.date.date()
            birthday_this_year = birthday.replace(year=today.year)
        
            # If the birthday has already passed this year, check the next year
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            # Check if the birthday falls within the next N days
            if today <= birthday_this_year <= delta_date:
                congratulation_date = birthday_this_year
                # If the birthday falls on a Saturday, move it to the following Monday
                if congratulation_date.weekday() == 5:  # Saturday
                    congratulation_date += timedelta(days=2)
                # If the birthday falls on a Sunday, move it to the following Monday
                elif congratulation_date.weekday() == 6:  # Sunday
                    congratulation_date += timedelta(days=1)
            
                congratulations_list.append({
                    "name": name,
                    "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
                })
        return congratulations_list
    
    def phone_exists(self, phone: str) -> bool:
        for record in self.data.values():
            for p in record.phones:
                if p.value == phone:
                    return True
        return False
    
    def email_exists(self, email: str) -> bool:
        for record in self.data.values():
            for p in record.emails:
                if p.value.lower() == email.lower():
                    return True
        return False
