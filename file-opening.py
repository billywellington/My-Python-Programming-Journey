try:
    with open("wife3.txt") as file:
        print(file.read())

except Exception:
    print("Sorry! File not found")