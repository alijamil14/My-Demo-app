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



if st.checkbox('Male'):
    st.text('You are Male')
if st.checkbox('Female'):
   st.text('You are Female')

status = st.radio("Select Gender:", ('Male', 'Female'))
if status == 'Male':
    st.success('You are brave...')
else:
    st.warning('You are clever')


# hobby = st.select("Hobbies:", ['Dancing', 'Reading', 'Sports'])
# st.write("Your hobby is:" , hobby)

hobby = st.multiselect("Hobbies:", ['Dancing', 'Reading', 'Sports'])
st.write("Your hobby is:" , hobby)

st.button("CLice Me For Save", type='primary')


hobby = st.selectbox("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports'])
 
# print the selected hobby
st.write("Your hobby is: ", hobby)

hobbies = st.multiselect("Hobbies: ",
                         ['Dancing', 'Reading', 'Sports'])
 
# write the selected options
st.write("You selected", len(hobbies), hobbies, 'hobbies')

if st.button("Click me for no reason", type='primary'):
    st.write('Hello')

level = st.slider("Select the level", 1, 10)