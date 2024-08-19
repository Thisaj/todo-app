FILEPATH = "todos.txt"
def get_todos(filename=FILEPATH):
    with open(filename, "r") as file:
        todos = file.readlines()
    return todos

def set_todos(todos, filename=FILEPATH):
    """please list
    :param todos: todos
    :param filename: todos 1
    :return: todos
    """
    with open(filename, "w") as file:
        file.writelines(todos)