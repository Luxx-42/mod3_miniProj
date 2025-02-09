# Mini project mod 3 CLI

# Add a new contact
def add_contact(contacts):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    additional = input("Enter any additional information: ")
    
    contacts[phone] = {"name": name, "phone": phone, "email": email, "additional": additional}
    print("Contact added successfully!\n----------" )

# Edit existing contact
def edit_contact(contacts):
    phone = input("\nEnter the phone number of the contact to edit: ")
    if phone in contacts:
        field = input("Enter the field to edit (name, phone, email, additional): ").lower()
        if field in contacts[phone]:
            new_value = input(f"Enter the new value for {field}: ")
            if field == "phone":
                contact = contacts.pop(phone)
                contact[field] = new_value
                contacts[new_value] = contact
            else:
                contacts[phone][field] = new_value
            print("Contact updated successfully!")
        else:
            print("Field not found.")
    else:
        print("Contact not found.")

# Delete a contact
def delete_contact(contacts):
    phone = input("Enter the phone number of the contact to delete: ")
    if phone in contacts:
        del contacts[phone]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# Search for a contact
def search_contact(contacts):
    search_term = input("Enter name, phone number, or email to search: ").lower()
    for phone, details in contacts.items():
        if search_term in details["name"].lower() or search_term in phone.lower() or search_term in details["email"].lower():
            print(f"Found: {details['name']} - Phone: {phone}, Email: {details['email']}")
            return
    print("No contact found matching that search term.")

# Display contacts
def display_contacts(contacts):
    if not contacts:
        print("No contacts to display.")
        return
    for phone, details in contacts.items():
        print(f"Name: {details['name']}, Phone: {phone}, Email: {details['email']}")

# Export contacts
def export_contacts(contacts):
    if not contacts:
        print("There are no contacts to export.")
        return  
    filename = input("Enter the filename to export contacts (e.g., contacts.txt): ")
    try:
        with open(filename, 'w') as file:
            for phone, details in contacts.items():
                file.write(f"Phone: {phone}\n")
                for key, value in details.items():
                    file.write(f"  {key}: {value}\n")
                file.write("\n")
        print(f"Contacts have been exported to {filename}")
    except IOError:
        print("An error occurred while writing to the file.")

# Import contacts
def import_contacts(contacts):
    filename = input("Enter the filename to import contacts from (e.g., contacts.txt): ")
    try:
        with open(filename, 'r') as file:
            current_contact = None
            for line in file:
                line = line.strip()
                if not line:  
                    continue
                
                if line.startswith("Phone:"):
                    current_contact = {}
                    phone = line.split(':', 1)[1].strip()
                    contacts[phone] = current_contact
                elif current_contact is not None:
                    key, value = line.split(':', 1)
                    current_contact[key.strip()] = value.strip()
        print(f"Contacts have been imported from {filename}")
    except IOError:
        print("An error occurred while reading the file.")
    except ValueError:
        print("Error in file format.")

# Used a for loop for the menu (UI).
menu = {
    "1": "Add a new contact",
    "2": "Edit an existing contact",
    "3": "Delete a contact",
    "4": "Search for a contact",
    "5": "Display all contacts",
    "6": "Export contacts to a text file",
    "7": "Import contacts from a text file",
    "8": "Quit"
    }

contacts = {}

while True:

    print("Welcome to the Contact Management System!\nMenu:\n----------")

    # Menu for loop
    for key, value in menu.items():
        print(f"{key}. {value}")
    choice = input("\nPlease enter your choice (1-8): ")

    # Handling the choices
    if choice == '1':
        add_contact(contacts)
 
    elif choice == '2':
        edit_contact(contacts)

    elif choice == '3':
        delete_contact(contacts)

    elif choice == '4':
        search_contact(contacts)

    elif choice == '5':
        display_contacts(contacts)

    elif choice == '6':
        export_contacts(contacts)

    elif choice == '7':
        import_contacts(contacts)

    elif choice == '8':
        print("Thank you for using the Contact Management System. Goodbye!")
        break

    else:
        print("Invalid option, please try again.")
