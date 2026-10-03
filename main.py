import streamlit as st

st.title('Welcome to Corvit HCCDA-AI')
st.write('We are learning Python angauige')
st.write('We are learning UV Platform')
st.header('Its my header')
st.subheader('Welcome Bro')
st.text('Hi its my first text')
st.write('2')   #will show output according to datatype
st.write('Ali')   #will show output according to datatype
st.success("Logged on Successfully")
st.warning("Dont add Data in it")
st.info("for more info")
st.error('This is an error')
st.exception("exp")
st.checkbox('Show/Hide')
st.t



if st.checkbox('Male'):
    st.text('You are Male')
if st.checkbox('Female'):
   st.text('You are Female')

status = st.radio("Select Gender:", ('Male', 'Female'))
if status == 'Male':
    st.success('You are brave...')
else:
    st.warning('You are clever')

st.video(URL)

name = st.text_input('Enter your name')
st.write(name)