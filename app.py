import streamlit as st
import pandas as pd

st.write("""
# Two Number Divide App
This app divides two number
""")
#Get Input

st.header('User Input')

def user_input_features():
    number_1 = st.number_input("Number_1")
    number_2 = st.number_input("Number_2")
    
    data = {'Number_1': number_1,
            'Number_2': number_2
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()


for col in df.columns:
    if df[col].dtype != 'float64':
        df[col] = df[col].values.astype('float64')

st.table(df)

Result=df.number_1/df.number_2

#Model Inferencing

st.subheader('Result:')

if (df.number_2 != 0):
    Result=df.number_1/df.number_2
    st.write(Result)
else:
    st.write("Second Number is zero!, hence not divisible.")
