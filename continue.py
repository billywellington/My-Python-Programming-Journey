phone_number  = "123-4546-789"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")