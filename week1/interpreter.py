def main():
    user_input = ((input("Expression : ")).strip()).split(" ")
    
    match user_input[1] :
        case "+" :
            add(float(user_input[0]), float(user_input[2]))
        case "-" :
            subtract(float(user_input[0]), float(user_input[2]))
        case "*" :
            multiply(float(user_input[0]), float(user_input[2]))
        case "/" :
            divide(float(user_input[0]), float(user_input[2]))

def add(x, y):
    return(print(x + y))

def subtract(x, y):
    return(print(x - y))

def multiply(x, y):
    return(print(x * y))

def divide(x, y):
    return(print(x / y))

main()