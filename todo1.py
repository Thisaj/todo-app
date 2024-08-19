# operator >
# operator <
# operator >=
# operator <=
# operator == مساوی
# operator != نامساوی

# password = input("Enter a password: ")
# while password != "123456":
#     print("password is incorrect")
#     password = input("Enter a password: ")


# password = input("Enter a password: ")
# while password != "123456":
#     print("your password is incorrect")
#     password = input("enter your password: ")
# print("your password is correct")


# x = 1
# while x <= 6:
#   print(x)
#   x=x+1


# user_prompt = "enter a todo: "
#
# todos = []
#
# while True:
#     todo = input(user_prompt)
#     todos.append(todo)
#     print(todos)


user_prompt = "enter a todo: "
todos = []

while True:
    user_action = input("type add, show, edit or exit: ")

    match user_action:
        case "add":

            # file = open("todos.txt", "r")
            # todos = file.readlines()
            # file.close()

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todo = input("enter a todo: ")+"\n"
            todos.append(todo)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            # file = open("todos.txt", "w")
            # file.writelines(todos)
            # file.close()

        case "show":

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            # file = open("todos.txt", "r")
            # todos = file.readlines()
            # file.close()

            for index, todo in enumerate(todos):
                todo = todo.strip("\n")
                print(f"{index + 1}-{todo.capitalize()}")



        case "edit":

            number = input("enter number of todo to edit: ")
            number = int(number)
            todos[number - 1] = input("new todo: ")+"\n"

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "complete":

            number = input("enter number of todo to complete: ")
            todos.pop(int(number) - 1)

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "exit":
            break

print("done!")