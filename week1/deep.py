answer = input("What is the answer to the Great Question of Life, the Universe and Everything ? ")

#Short way
print("Yes" if answer in {"42", "forty-two", "forty two"} else "No")

# alt way
# match answer :
#     case "42" | "forty-two" | "forty two" :
#         print("Yes")
#     case _:
#         print("Wrong")