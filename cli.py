# import PySimpleGUI
import functions

while True:
    user_response = input("Enter add,edit,complete,show:")

    if user_response.startswith("add"):
        todo = user_response[4:]

        todos = functions.to_get_todo()

        todos.append(todo + '\n')

        functions.to_write_todo(todos)

    elif user_response.startswith("show"):
        
        todos = functions.to_get_todo()

        for i, value in enumerate(todos):
            value = value.strip("\n")
            to_print = f"{i+1}-{value}"
            print(to_print)

    elif user_response.startswith("edit"):
        try:
            number = int(user_response[5:])
            number = number - 1

            todos = functions.to_get_todo()

            new_todo = input("Enter the new todo:")
            todos[number] = new_todo + "\n"

            functions.to_write_todo(todos)

        except ValueError:
            print("The value you entered is not valid")
            continue

    elif user_response.startswith("complete"):
        try:

            number = int(user_response[9:])
            number = number - 1

            todos = functions.to_get_todo()

            todo_removed = todos[number].strip("\n")
            todos.pop(number)

            functions.to_write_todo(todos)

            print(f"{todo_removed} has been removed")

        except ValueError:
            print("The value you entered is not valid")
            continue

        except IndexError:
            print("The value you entered is not valid")
            continue

    elif user_response.startswith("exit"):
        print("Exiting the app")
        exit()

    else:
        print("Enter a legal command from the given options:")
        continue


