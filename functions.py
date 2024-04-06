FILEPATH ="todo.txt"

def to_get_todo():
    with open(FILEPATH, "r") as file:
        todos = file.readlines()
        return todos

def to_write_todo(todos):
    with open(FILEPATH, "w") as file:
        file.writelines(todos)