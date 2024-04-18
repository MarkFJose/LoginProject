

def generate_login(first_name, last_name,bcit_id):
    """ A function that generates a login password
    :param first_name: user's first name
    :param last_name: user's last name
    :param bcit_id: user's BCIT ID
    :returns: the default login password
    """
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    print("generate default login password:")
    if len(first_name) < 3:
        pass
    else:
        first_name = first_name[0:3]
    if len(last_name) < 3:
        pass
    else:
        last_name = last_name[0:3]
    if len(bcit_id) < 3:
        pass
    else:
        bcit_id = bcit_id[-3:]
    tokens = [first_name,last_name,bcit_id]
    default_login = "".join(tokens)
    print(default_login)

def change_password():
    """
    A function that prompts a user to enter a new password
    :return: the new password
    """
    valid = False
    password = input("Enter your new password")
    while not valid:
        print(password.isalnum())
        if not len(password) >= 7:
            print("The password must be at least 7 characters")
            pass
        elif not any(uppercase_char.isupper() for uppercase_char in password):
            print("The password must have at least one uppercase character")
            pass
        elif not any(lowercase_char.islower() for lowercase_char in password):
            print("The password must have at least one lowercase character")
            pass
        elif not any(numeric_characters.isdigit() for numeric_characters in password):
            print("The password must have at least one numerical digit")
            pass
        elif not password.isalnum():
            print("The password must not have special characters")
            pass
        elif password.isspace():
            print("The password must not have any spaces")
            pass
        else:
            valid = True
            print("Your password meets password requirements")
            return password
        print("Password must be at least seven characters long, contain at least one numeric digit, must not contain "
              "special characters or spaces.")
        password = input("Please enter another password:")



def main():
    pass

if __name__ == "__main__":
    main()