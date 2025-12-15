def main():
    camel = input("camelCase: ")
    print("snake_case: ", end="")
    
    for ch in camel:
        print("_" + ch.lower() if ch.isupper() else ch, end="")

if __name__ == "__main__":
    main()