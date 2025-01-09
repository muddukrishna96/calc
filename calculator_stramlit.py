# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 17:46:36 2025

@author: muddu krishna
"""

import streamlit as st

def calculate(option, num1, num2):
    if option == "Add":
        return num1 + num2
    elif option == "Subtract":
        return num1 - num2
    elif option == "Multiply":
        return num1 * num2
    elif option == "Divide":
        return num1 / num2 if num2 != 0 else "Division by zero error"
    else:
        return "Invalid Option"

# Streamlit UI
def main():
    st.title("Simple Calculator")

    # Inputs for numbers
    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number:", value=0.0)

    # Options for operations
    operation = st.selectbox("Choose an operation:", ["Add", "Subtract", "Multiply", "Divide"])

    # Calculate result on button press
    if st.button("Calculate"):
        result = calculate(operation, num1, num2)
        st.write(f"The result is: {result}")

if __name__ == "__main__":
    main()
