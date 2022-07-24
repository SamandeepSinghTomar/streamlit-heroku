#div

import streamlit as st

st.title('Two-Number Division')
a= st.number_input('Number A')
b =st.number_input('Number B')
if b == 0:
  a1=st.write(f'A/B = Undefined')
else:
  a1=st.write(f'A/B = {a/b}')
print(a1)
