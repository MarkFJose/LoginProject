# data_format.py

def get_book_info():
    """
    A function that gets user input to get the details of a book
    :return: A string that includes the book details
    """
    book_title = input("Enter the book title:")
    book_isbn = input("Enter the book ISBN:")
    book_author_last_name = input("Enter the author's last name:")
    book_publisher = input("Enter the book publisher:")
    year_published = input("Enter the year published:")
    if not (year_published >= 2024 and year_published < 1900):
        raise Exception("Please enter a year between 1900 and 2024")
    book_price_in_usd = float(input("Enter the book price in American dollars:"))

    thisdict = {
        "title": book_title,
        "isbn" : book_isbn,
        "author" : book_author_last_name,
        "publisher" : book_publisher,
        "year_published" : year_published,
        "price" : book_price_in_usd
    }

    for i in thisdict:
        i.strip().title()

    book_info = f"{book_title}/{book_isbn}/{book_author_last_name}/{book_publisher}/{year_published}/{book_price_in_usd:.2f}"
    book_info = book_info.strip().title()
    return book_info

def to_csv_format(book_info):
    """
    A function that takes a string of information and returns it in CSV format
    :param book_info: A string of information about the book
    :return: A string in CSV format
    """
    csv_format = book_info.replace("/", ",")
    return csv_format

def to_JSON_format(csv_format):
    """
    A function that take a string of provided information and returns that information into JSON format
    :param csv_format: Gets a string including the details of book in csv_format 
    :return: Returns book details in JSON format 
    """
    #finds book title
    book_info = csv_format
    separator = book_info.find(",")
    book_title = book_info[0:separator]
    book_info = book_info[separator+1:]
    # finds book isbn
    separator = book_info.find(",")
    book_isbn = book_info[0:separator]
    book_info = book_info[separator+1:]
    # finds book author last name
    separator = book_info.find(",")
    book_author_last_name = book_info[0:separator]
    book_info = book_info[separator+1:]
    # find book publisher
    separator = book_info.find(",")
    book_publisher = book_info[0:separator]
    book_info = book_info[separator+1:]
    # find year published
    separator = book_info.find(",")
    year_published = book_info[0:separator]
    book_info = book_info[separator+1:]
    # find book price in usd
    book_price_in_usd = str(book_info)
    # takes strings and creates a new string in JSON format
    json_format = f'{{"Book Title": "{book_title}",' \
                  f'"Book ISBN": "{book_isbn}",' \
                  f'"Author Last Name": "{book_author_last_name}",' \
                  f'"Book Publisher": "{book_publisher}",' \
                  f'"Year Published":"{year_published}",' \
                  f' "Book Price In American": {book_price_in_usd} }}'
    return json_format



def main():
    book_info = get_book_info()
    # print(book_info)
    csv_format = to_csv_format(book_info)
    print("CSV Format:")
    print(csv_format)
    json_format = to_JSON_format(csv_format)
    print("JSON Format:")
    print(json_format)



if __name__ == '__main__':
    main()