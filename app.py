import streamlit as st

st.write("""
# Two Number Divide App
This app divides two number
""")
#Get Input

st.header('User Input')

def user_input_features():
    number_1 = st.number_input("Number_1")
    number_2 = st.number_input("Number_2")
    
    return number_1,number_2

n1, n2 = user_input_features()

st.subheader('Result:')

if (n2 != 0):
    Result=n1/n2
    st.write(Result)
else:
    st.write("Second Number is zero!, hence not divisible.")
