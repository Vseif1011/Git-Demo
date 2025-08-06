Library = {
    'Books' : [],
    'Year of publishing' : [],
}

def add_book(Book_Name, Year_of_Publishing):
 
    Library['Books'].append(Book_Name)
    Library['Year of publishing'].append(Year_of_Publishing)
    print(f"{Book_Name} Published at {Year_of_Publishing} has been added to the library")
    

def search(Book_name):
    for book in Library['Books']:
        if book.lower() == Book_name.lower():
            print(f"The book ({Book_name}) is available")
            return True
    
    print(f"The book ({Book_name}) isn't availble")
    return False


def sell(Book_Name):
    for i,book in enumerate(Library['Books']):
        if book.lower() == Book_Name.lower():
            del Library['Books'][i]
            del Library['Year of publishing'][i]
            print(f"The book ({Book_Name}) have been sold successfully")
            return 
    print(f"The book ({Book_Name}) isn't available for selling")


def print_books():
    for i in range(len(Library["Books"])):
        print(f'{Library["Books"][i]} Published at: {Library["Year of publishing"][i]}')



print("Adding Books:")
add_book("1984", 1949)
add_book("Sapiens", 2011)
add_book("Dune", 1965)
add_book("Jane Eyre", 1847)
add_book("The Lord of the Rings", 1954)

print("\n Searching for Books:")
search("Sapiens")
search("The Hobbit") 
search("The Lord of the Rings")

print("\n Printing Library:")
print_books()

print("\n Selling Books:")
sell("Dune")  
sell("Dune")  

print("\n Printing Library After Selling:")
print_books()

