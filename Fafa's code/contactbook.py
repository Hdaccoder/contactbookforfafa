import datetime
datetime.date.today().strftime("%B %d, %Y")

def search (query):
    query = query.lower()
    contlist = open("contactlist.txt")
    for line in contlist:
        if query in line:
            return line
    contlist.close()
    mainmenu()

def addcontact(fname, sname, email, number, address):
    contlist = open("contactlist.txt", "a")
    contlist.writelines(fname + " " + sname + " " + email + " " + number + " " + address + " Date added: " + datetime.date.today().strftime("%d - %m - %Y"))
    print ("Contact added.")
    mainmenu()

def mainmenu():
    task = str(input("Welcome to the main menu, What would you like to do?\n[1]Add a contact\n[2]Search for contact"))
    task = task.lower()

    if task == "1" or task == "add a contact" or task == "add contact":
        firstname = str(input("What is their first name?: "))
        surname = str(input("What is their last name?: "))
        elecmail = str(input("What is their email?: "))
        while "@" not in elecmail and "." not in elecmail:
            elecmail = str(input("What is their email?: "))
        num = str(input("What is their number?: "))
        addr = str(input("What is their address?: "))
        addcontact(firstname, surname, elecmail, num, addr)
    elif task == "2" or task == "search":
        query = str(input("What is your search?: "))
        search(query)
    else:
        print("That is not a valid input")
        mainmenu()

mainmenu()
        