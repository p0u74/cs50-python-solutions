def main():
    time = ((input("What time is it ? (##:## format, 24 hours) : ")).strip()).split(":")
    convert(time)

def convert(time):
    time = float(time[0])+(float(time[1])/60)
    print("breakfast time" if 7 <= time <= 8 else "lunch time" if 12 <= time <= 13 else "dinner time" if 18 <= time <= 19 else "No food")

if __name__ == "__main__":
    main()