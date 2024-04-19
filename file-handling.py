text = "\nThis has been appended\n"

try:
    with open("wife3.txt", "a") as file:
        file.write(text)

except Exception as error:
        print(error)
