# contacts.py - A simple contact book using dictionaries 

# Each contact is a dictionary, the whole book is a dictionary of contacts 
contacts = {
    "alice": {
        "full_name": "Alice Johnson",
        "phone": "555-0101",
        "email": "alice@example.com"
    },
    "bob": {
        "full_name": "Bob Smith",
        "phone": "555-0202",
        "email": "bob@example.com"
    }
}

def display_contacts():
    """Print all contacts in a formatted way."""
    print("" + "=" * 40)
    print("       Contact Book")
    print("=" * 40)

    if not contacts:
        print("No contacts yet.")
        return
    
    for key, info in contacts.items():
        print(f"    {info['full_name']}")
        print(f"    Phone: {info['phone']}")
        print(f"    Email: {info['email']}")

    print(f"Total Contacts: {len(contacts)}")
    print("=" * 40)

display_contacts()

# Look up specific contact
search = input("Look up a contact (enter first name): ").lower()

contact = contacts.get(search) 

if contact: 
    print(f"Found: {contact['full_name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
else:
    print(f"No contact found for '{search}'.")

# Add new contact
print("--- Add New Contact ---")
new_key = input("First Name (for lookup): ").lower()
new_full = input("Full Name: ")
new_phone = input("Phone: ")
new_email = input("Email: ")                 

contacts[new_key] = {
    "full_name": new_full,
    "phone": new_phone, 
    "email": new_email
}

print(f"{new_full} added successfully!")
display_contacts()
