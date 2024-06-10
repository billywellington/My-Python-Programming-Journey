line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
# position = input()  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇


position = "A1"

column = position[0]
row = position[1]

if row == 1:
    if column == "A":
        line1 = ['X', '⬜️', '️⬜️']
    elif column == "B":
        line1 = ['⬜️', 'X', '️⬜️']
    else:
        line1 = ['⬜️', '⬜️', '️X']

elif row == 2:
    if column == "A":
        line2 = ['X', '⬜️', '️⬜️']
    elif column == "B":
        line2 = ['⬜️', 'X', '️⬜️']
    else:
        line2 = ['⬜️', '⬜️', '️X']

else:
    if column == "A":
        line3 = ['X', '⬜️', '️⬜️']
    elif column == "B":
        line3 = ['⬜️', 'X', '️⬜️']
    else:
        line3 = ['⬜️', '⬜️', '️X']

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")