
print('Welcome to XWYZ Park, the world of rollercosters!')
height = int(input("What is your height in cm? "))

if height < 120:
    print("Come back when you're a bit taller :))")

else:
    print("Tall enough to have a fun ride!")
    age = int(input("How old are you? "))
    if age >= 21 and age <= 44:
        bill = 12.50
        print("Please pay the adults price, $12.50")
    elif age <= 10:
        bill = 9.50
        print("Please pay the kids price, $9.50")
    elif age >= 45 and age <= 55:
        bill = 0.00
        print(f"Your bill is ${bill}")
    else:
        bill = 18.00
        print("Kindly pay the teen price, $18.00")

    photos = input("Do you want a picture? Y or N ")
    if photos == "Y":
        if age >= 45 and age <= 55:
            bill = 0

        elif age <= 44 and age >= 56:
            bill += 3
            bill = float(bill)

    print(f"Your total bill is ${bill}")

