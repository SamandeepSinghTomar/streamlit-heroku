import streamlit as st
string = "Two Numbers Division"
st.set_page_config(page_title=string)

st.title('Two Numbers Division')
x = st.number_input('Enter number 1')
y = st.number_input('Enter number 2')
if (y!=0):
    st.write("Result:")
    st.write(x/y)
else:
    st.write("Zero Division Error!!")
