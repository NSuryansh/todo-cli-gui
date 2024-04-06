import streamlit as st
import functions

todos = functions.to_get_todo()

st.title("My ToDo list")


def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo)
    functions.to_write_todo(todos)


for todo in todos:
    st.checkbox(todo, key=todo)

st.text_input(placeholder="Enter the todo here", label="", key="new_todo", on_change=add_todo)


