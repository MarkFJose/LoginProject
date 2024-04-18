import login



def main ():
    first_name = input("Enter your first name:")
    last_name = input("Enter your last name:")
    bcit_id = input("Enter your BCIT ID:")
    current_password = login.generate_login(first_name,last_name,bcit_id)
    print(current_password)
    password = login.change_password()
    print(current_password)

if __name__ == "__main__":
    main()