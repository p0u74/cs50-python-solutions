C = 3e8 # 3e8 = 300000000

def main():
    formula(float(input("Enter value of mass to calculate energy for you : ")))

def formula(mass):
    energy = mass * C * C
    return(print(f"Energy is {energy}"))

main()