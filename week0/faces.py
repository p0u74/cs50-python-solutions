def main():
    convert(input("Write something for me : "))
    
def convert(text):
    text = (text.replace(":)", "🙂")).replace(":(", "🙁")
    return(print(text))

main()