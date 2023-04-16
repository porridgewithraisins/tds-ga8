import streamlit as st

st.title("Largest Number Finder")
st.write("Enter three numbers and find the largest among them.")

num1 = st.number_input("Enter number 1", value=0)
num2 = st.number_input("Enter number 2", value=0)
num3 = st.number_input("Enter number 3", value=0)

if num1 == num2 == num3:
    st.write("All three numbers are equal.")
else:
    st.write("The largest number is:", max(num1, num2, num3))
