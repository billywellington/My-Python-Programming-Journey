name1 = "Catherine Zeta-Jones"
name2 = "Michael Douglas"

#words to check : TRUE & LOVE
true_count = love_count = 0
t_count = r_count = u_count = e_count = 0
l_count = o_count = v_count = e_love_count = 0

#checking for word "TRUE" on name 1

t_count = name1.count("t")
r_count = name1.count("r")
u_count = name1.count("u")
e_count = name1.count("e")


true_count = t_count + r_count + u_count + e_count


#checking for word "TRUE" on name 2

t_count = name2.count("t")
r_count = name2.count("r")
u_count = name2.count("u")
e_count = name2.count("e")

true_count = true_count + t_count + r_count + u_count + e_count

#checking for word "LOVE" on name 1

l_count = name1.lower().count("l")
o_count = name1.lower().count("o")
v_count = name1.lower().count("v")
e_love_count = name1.lower().count("e")

love_count = l_count + o_count + v_count + e_love_count

#checking for word "LOVE" on name 2

l_count = name2.lower().count("l")
o_count = name2.lower().count("o")
v_count = name2.lower().count("v")
e_love_count = name2.lower().count("e")

love_count = love_count + l_count + o_count + v_count + e_love_count

str_score = str(true_count) + str(love_count)
int_score = int(str_score)
#
#
if 40 < int_score < 50:
    print(f"Your score is {int_score}, you are alright together.")
elif 10 < int_score > 90:
    print(f"Your score is {int_score}, you go together like coke and mentos.")
else:
    print(f"Your score is {int_score}.")