import streamlit as st
import modules.cli as functionsss

todos = functionsss.get_todos()

def add_todo():
    todos = functionsss.get_todos()
    todo= st.session_state["new_todo"]
    todos.append(todo + "\n")
    functionsss.set_todos(todos)

def remove_todo(todo):
    todos.remove(todo)
    functionsss.set_todos(todos)
    st.rerun()


st.title("My todo app")
st.subheader("This is a todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"checkbox_{index}")
    if checkbox:
        remove_todo(todo)



st.text_input(label="", placeholder="enter new todo: ",
              on_change=add_todo,key="new_todo",)
print("hello")
st.session_state
st.session_state["new_todo"]