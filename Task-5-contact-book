contacts = []
def add_contact():
    print("-" * 40)
    print(" ADD CONTACT")
    print("-" * 40)
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully!")
def view_contacts():
    if len(contacts) == 0:
        print("No contacts available.")
    else:
        print("-" * 40)
        print(" CONTACT LIST")
        print("-" * 40)
        for number, contact in enumerate(contacts, start=1):
            print(f"{number}. Name : {contact['name']}")
            print(f" Phone : {contact['phone']}")
            print("-" * 40)
def search_contact():
    if len(contacts) == 0:
        print("No contacts available.")
        return
    search = input("Enter name or phone number to search: ").lower()
    found = False
    for contact in contacts:
        if (search == contact["name"].lower()
                or search == contact["phone"]):
            found = True
            print("-" * 40)
            print(" CONTACT FOUND")
            print("-" * 40)
            print(f"Name : {contact['name']}")
            print(f"Phone : {contact['phone']}")
            print(f"Email : {contact['email']}")
            print(f"Address : {contact['address']}")
    if found == False:
        print("Contact not found.")
def update_contact():
    if len(contacts) == 0:
        print("No contacts available.")
        return
    phone = input("Enter phone number of contact to update: ")
    found = False
    for contact in contacts:
        if phone == contact["phone"]:
            found = True
            print("Enter new contact details:")
            name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact["name"] = name
            contact["phone"] = new_phone
            contact["email"] = email
            contact["address"] = address
            print("Contact updated successfully!")
            break
    if found == False:
        print("Contact not found.")
def delete_contact():
    if len(contacts) == 0:
        print("No contacts available.")
        return
    phone = input("Enter phone number of contact to delete: ")
    found = False
    for contact in contacts:
        if phone == contact["phone"]:
            contacts.remove(contact)
            found = True
            print("Contact deleted successfully!")
            break
    if found == False:
        print("Contact not found.")
while True:
    print("\n" + "=" * 40)
    print(" CONTACT BOOK")
    print("=" * 40)

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    try:
        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            add_contact()

        elif choice == 2:
            view_contacts()

        elif choice == 3:
            search_contact()

        elif choice == 4:
            update_contact()

        elif choice == 5:
            delete_contact()

        elif choice == 6:
            print("Exiting Contact Book. Thank you!")
            break

        else:
            print("Invalid choice. Enter a number from 1-6.")

    except ValueError:
        print("Invalid input. Please enter a number from 1-6.")
