import json
phonebook={"nishant":8340324646,
        "mommy":73618980,
        "papa":0000000000 }
    # print(phonebook["nishant"])
while True:
    all=input('''    Add Contact:
    Search Contact:
    Contact List:
    Edit Contact's Name:
    Edit Contact's Number:
    Delete Contact:
    Exit:
    =>''').lower()
    if all=="add contact":
        add_contact=input("Name:",)
        add_contact2=input("Contact Number:",)
        phonebook[add_contact]=add_contact2
        print(add_contact,"added to contacts")
        # print(phonebook)
    elif all=="search contact":
        search=input("Search Contact:",)
    # while search not in (phonebook):
        print(search,"Contact No:",phonebook.get(search))
    elif all=="contact list":
        print('''~~~~~Contact List~~~~~''',json.dumps(phonebook, indent=4))
    elif all=="edit contact's name":
        old_name=input("Enter the name to be edited:")
        edit_name=input("New Name:")
        phonebook[edit_name]=phonebook.pop(old_name)
        print(f"{old_name} edited to {edit_name}")
    elif all=="edit contact's number":
        name_ed=input("Enter the name to edit contact's number:")
        new_number=input("New Number:")
        phonebook[name_ed]=new_number
        print(f"{name_ed}number updated to:{new_number}")
    elif all=="delete contact":
        delete=input("Delete Contact:")
        phonebook.pop(delete)
        print(f"{delete} deleted from contacts")
    if all=="exit":
        break