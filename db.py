import mysql.connector
class Connection:
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                database="login1",
                password="")
            self.mycursor = self.mydb.cursor()
        except:
            print("Database connection error")
            import sys
            sys.exit(0)
        else:
            print("Database connection successful")
    
    def register(self,name,email,password):
        try:
            self.mycursor.execute("""
        INSERT INTO `login` (`ID`, `Name`, `Email`, `Password`) VALUES (NULL, '{}', '{}', '{}\r\n')

    """.format(name, email, password))
            self.mydb.commit()
        except:
            return -1
        else:
            return 1
        
    def search(self, email, password):
        try:
            data = self.mycursor.execute("""
        SELECT * FROM `login` WHERE `Email` = '{}' AND `Password` = '{}'""".format(email, password))
        except:
            print("your password and email is incorrect please try again !")
        else:
            print("your password and email is correct")
            print(data)
            
            