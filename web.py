import streamlit as st
from db import Connection

st.title("Login Page")

class LoginPage:
    def __init__(self):
        self.window()
        self.mydb = Connection()

    def window(self):
        self.username = st.text_input("Username")
        self.password = st.text_input("Password", type="password")
        self.email = st.text_input("Email Address")
        self.login = st.button("Login")
        self.signup = st.button("Sign Up")
        self.forgot_password = st.button("Forgot Password")

        if self.login:
            if self.username.strip() == "" or self.password.strip() == "" or self.email.strip() == "":
                st.error("Please fill all the fields.")
            else:
                self.mydb = Connection()
                user = self.mydb.register(self.username, self.email, self.password)
                if user:
                    st.success("Registration Successful")
                else:
                    st.error("Registration Failed")

        if self.signup:
            if self.username.strip() == "" or self.password.strip() == "":
                st.error("Please enter username and password.")
           
objects = LoginPage()