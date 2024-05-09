import sys
from db import Connection
class flipcart:
    def __init__(self):
        self.menu()

    def menu(self):
        self.conn = Connection() 
        option = input("""
                1 Enter for register
                2 Enter for login
                3 Enter for exit

""")
        if option == "1":
            self.register()
        elif option == "2":
            self.login()
        elif option == "3":
            print("Thank you")
            sys.exit(1000)
        else:
            self.menu()
        
    def register(self):
        name = input("enter name :")
        email = input("enter email :")
        password = input("enter password :")
        response =self.conn.register(name,email,password)
        if response:
            print("Successfully registered")
        else:
            print("Something went wrong")
            self.menu()
    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        response = self.conn.search(email,password)
        
        
    
obj = flipcart()