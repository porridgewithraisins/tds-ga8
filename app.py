import streamlit as st

def find_largest_number(num1, num2, num3):
    """Find the largest number among three given numbers."""
    largest_number = max(num1, num2, num3)
    return largest_number

# Streamlit app
def app():
    # Set up the title and description
    st.title("Largest Number Finder")
    st.write("Enter three numbers and find the largest among them.")

    # Get user input for three numbers
    num1 = st.number_input("Enter number 1", value=0)
    num2 = st.number_input("Enter number 2", value=0)
    num3 = st.number_input("Enter number 3", value=0)

    # Find the largest number
    largest_number = find_largest_number(num1, num2, num3)

    # Display the result
    if num1 == num2 == num3:
        st.write("All three numbers are equal.")
    else:
        st.write("The largest number is:", largest_number)

# Run the Streamlit app
if __name__ == '__main__':
    app()
