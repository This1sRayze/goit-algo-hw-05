# Завдання номер 1
def caching_fibonacci(n):
    cache = {}
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]   
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]     
    return fibonacci(n)



# Завдання номер 2
import re

def generator_numbers(text: str):
    for match in re.findall(r'\s(-?\d+\.\d+)\s', f' {text} '):
        yield float(match)

def sum_profit(text: str) -> float:
    return sum(generator_numbers(text))
         



# Завдання номер 3
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "This contact does not exist."   
        except IndexError:
            return "Enter user name."  

    return inner
    
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_phone(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    return "Contact not found."

@input_error
def phone_username(args, contacts):
    name = args[0]
    return contacts.get(name, "Contact not found.")

def all(contacts):
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_phone(args, contacts))    
        elif command == "phone":
            print(phone_username(args, contacts))
        elif command == "all":
            print(all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()