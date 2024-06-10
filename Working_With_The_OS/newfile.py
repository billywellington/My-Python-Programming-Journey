# You are going to write a program that tests the compatibility between two people.
#
# To work out the love score between two people:
#
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
#
# Then check for the number of times the letters in the word LOVE occurs.
#
# Then combine these numbers to make a 2 digit number.
#
# For Love Scores less than 10 or greater than 90, the message should be:
#
# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
#
# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:
#
# "Your score is *z*."
# e.g.
#
# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times
#
# R occurs 1 time
#
# U occurs 2 times
#
# E occurs 2 times
#
# Total = 5
#
# L occurs 1 time
#
# O occurs 0 times
#
# V occurs 0 times
#
# E occurs 2 times
#
# Total = 3
#
# Love Score = 53
#
# Print: "Your score is 53."

name1 = "Han Solo"
name2 = "Princess Leia Organa"

#words to check : TRUE & LOVE
true_count = 0
love_count = 0

if "t" in name1.lower():
    true_count +=1
if "r" in name1.lower():
    true_count +=1
if "u" in name1.lower():
    true_count +=1
if "e" in name1.lower():
    true_count +=1

if "t" in name2.lower():
    true_count +=1
if "r" in name2.lower():
    true_count +=1
if "u" in name2.lower():
    true_count +=1
if "e" in name2.lower():
    true_count +=1

#for word love

if "l" in name1.lower():
    love_count += 1
if "o" in name1.lower():
    love_count += 1
if "v" in name1.lower():
    love_count += 1
if "e" in name1.lower():
    love_count += 1

if "l" in name2.lower():
    love_count += 1
if "o" in name2.lower():
    love_count += 1
if "v" in name2.lower():
    love_count += 1
if "e" in name2.lower():
    love_count += 1

str_score = str(true_count) + str(love_count)
int_score = int(str_score)


if 40 < int_score < 50:
    print(f"Your score is {int_score}, you are alright together.")
elif int_score < 10 and int_score > 90:
    print(f"Your score is {int_score}, you go together like coke and mentos.")
else:
    print(f"Your score is {int_score}.")