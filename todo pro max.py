from modules.functionsss import set_todos, get_todos

text = """python file is okkk"""
# text = "\n\
#        python file\n\
#        is okkkk\n\
#         "
print(text)

user_prompt = "enter a todo: "
todos = []

while True:
    user_action = input("type add, show, edit or exit: ")

    if user_action.startswith("add"):

        todos = get_todos("todos.txt")

        todo = user_action[4:]+"\n"
        todos.append(todo)

        todos = set_todos(todos, "todos.txt")

        # TODO: add more functionality here

    elif user_action.startswith("show"):

        todos = get_todos("todos.txt")

        for index, todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{index + 1}-{todo.capitalize()}")

    elif user_action.startswith("edit"):
        try:

            todos = get_todos("todos.txt")
            number = int(user_action[5:])-1
            new_todo = input("inter new todo: ")+"\n"
            todos[int(number)] = new_todo
            todos = set_todos(todos, "todos.txt")
        except IndexError:
            print("your number is out of range")

    elif user_action.startswith("complete"):
        try:

            todos = get_todos("todos.txt")

            index = int(user_action[9:]) - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            message = f"todo {todo_to_remove} has been completed."
            print(message)

            todos = set_todos(todos, "todos.txt")
        except ValueError:
            print("your should inter a number")
        except IndexError:
            print("your number is out of range")

    elif user_action.startswith("exit"):
        break

    else:
        print("invalid input")

print("done!")