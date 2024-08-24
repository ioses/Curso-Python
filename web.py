import streamlit as st 
import functions

## Para ejecutar con streamlit: streamlit run web.py

todos = functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My ToDo App")
st.subheader("This is my ToDo App")
st.write("<h1>This app is to increase your <b>productivity<b>. </h1>", unsafe_allow_html=True) ##HTML solo se permite en el metodo Write

st.text_input(label ="", placeholder="Add new Todo", on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()




print("Hello")

st.session_state
