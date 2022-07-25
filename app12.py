#div

import streamlit as st

string="2NumberDivision"
st.set_page_config(page_title=string, page_icon="🧮")

st.title('Two-Number Division')
a= st.number_input('Number A')
b =st.number_input('Number B')
if b == 0:
  a1=st.write(f'Result = Undefined')
else:
  a1=st.write(f'Result = {a/b}')
print(a1)
