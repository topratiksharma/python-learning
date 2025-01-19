def greet(first_name):
    message = f"Hi there {first_name}"
    print(message)
    return message


greet("Pratik")


# xargs
def multiple(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiple(5, 2, 8, 6))


# xxargs
def save_user(**user):
    print(user)
    print(user["name"])


save_user(id=1, name="John", age=22)
