def hello(name, message):
    print("HELLO "+name, end = "\n"+message+"!")

def main():
    name = input("Enter your name = ")
    message = input("Enter your message = ")
    hello(name, message)

main()