# Quejano_DreamsFileManager

while True:

    print("\n===== DREAMS FILE MANAGER =====")
    print("1. Read inspiring messages")
    print("2. Add a new inspiring message")
    print("3. Rewrite the entire file")
    print("4. Exit")
    print("===============================\n") #pang kaartehan lang po 

    choice = input("Enter your choice:")
    
    print("=================================")

    if choice == "1":

        file = open("dreams.txt", "r")

        content = file.read()

        print("\n----- Inspiring Messages -----\n")
        print(content)
        print("==================================")
        
        file.close()
        
        
    

    elif choice == "2":

        message = input("\nEnter a new inspiring message: \n")

        file = open("dreams.txt", "a")

        file.write(message + "\n")
        print("===================================")    
        file.close()

        print("Message added successfully!")
        print("===================================") 
        
        
        
    elif choice == "3":

        confirm = input("Are you sure? (yes/no): ")

        if confirm.lower() == "yes":

            new_content = input("Enter new inspiring message: ")

            file = open("dreams.txt", "w")

            file.write(new_content + "\n")
            print("===================================")

            file.close()

            print("File rewritten successfully!")
            print("===================================")

        else:
            print("Rewrite cancelled.")
            
            
            
            

    elif choice == "4":

        print("Exiting program...")
        break





    else:

        print("Invalid choice. Please try again.")