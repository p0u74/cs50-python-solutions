greet = ((input("Greeting : ")).strip()).lower()

#Short way
print("0$" if "hello" in greet else "20$" if greet.startswith('h') else "100$")

# alt way
# if "hello" in greet :
#     print("0$")
# elif greet[0] == "h" :
#     print("20$")
# else :
#     print("100$")


