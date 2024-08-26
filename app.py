import streamlit as st

st.header('CALCULATOR')

x=st.number_input(label='enter a 1st number',value=0)

op=st.selectbox('select a opeator',
                options=['+','-','*','/'])

y=st.number_input(label='enter 2nd number',value=0)

btn=st.button('calculate')

if btn:
    if op=='+':
        st.subheader(x+y)
    elif op=='-':
        st.subheader(x-y)
    elif op=='*':
        st.subheader(x*y)
    else:
        st.subheader(x/y)


