from collections import UserDict
from datetime import datetime, timedelta
from .record import Record
from ..shared.error_handler.decorators import ValueExistsError

class AddressBook(UserDict):
    """Dictionary-based address book storage."""
        
    def add_record(self, record: Record):
        name = record.name.value
        if self.find(name):
            raise ValueExistsError("Contact already exists")
        self.data[name] = record

    def find(self, name: str):
        return self.data.get(name)
        
    def delete(self, name: str):
        if not self.find(name):
            raise KeyError("Contact not found")
        self.data.pop(name)

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        delta_date = today + timedelta(days=7)
        congratulations_list = []
    
        for name, value in self.data.items():
            if value.birthday is None:
                continue

            birthday = value.birthday.date.date()
            birthday_this_year = birthday.replace(year=today.year)
        
            # If the birthday has already passed this year, check the next year
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            # Check if the birthday falls within the next 7 days
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
        if not congratulations_list:
            return "The list is empty. No celebrations, only work!"
        return congratulations_list
    
    def phone_exists(self, phone: str) -> bool:
        for record in self.data.values():
            for p in record.phones:
                if p.value == phone:
                    return True
        return False

    def __str__(self):
        return (
        f"[green]Name:[/green] [cyan]{self.name.value}[/cyan][green]; [/green]"
        f"[green]Phones:[/green] [cyan]{', '.join(p.value for p in self.phones) if self.phones else 'No phones'}[/cyan][green]; [/green]"
        f"[green]Birthday:[/green] [cyan]{self.birthday.date.strftime('%d.%m.%Y') if self.birthday else 'No birthday'}[/cyan]"
    )