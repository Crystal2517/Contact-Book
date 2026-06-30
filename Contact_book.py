add_contact = {}
while True:
    print("""Choose an option: 
          1. Add Contact
          2. View Contact
          3. Exit""")
    option = input(">: ")
    
    if option == "1":
        number_of_contacts = int(input("Enter how many contacts you want to add: "))
        for x in range (number_of_contacts):
            contact = input("Enter contact name: ")
            number = (input("Enter phone number: "))
            add_contact[contact] = number

    elif option == "2":
        if not add_contact:
            print("No contacts found.")
        else:
            for key, value in add_contact.items():
                print(f"{key}: {value} ")
            
    elif option == "3":
        print("Goodbye!")
        break
    
    else:
        print("Invalid option. Please choose 1,2 or 3.")









