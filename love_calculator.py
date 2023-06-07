print("Welcome to the love Calculator !! ")
name1 = input("What is your name ? ")
name2 = input("what is your lover''s name ?  ")

# have to combine the names together
combined_string = name1 + name2
# convert all the names to lowercase
lower_case_name = combined_string.lower()

# checking how times T is showed up
t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")

# add all of them
true = t + r + u + e

# count the love
l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")

# add all of them
love = l + o + v + e

love_score = int(str(true)) + int(str(love))

if (love_score < 10) or (love_score >90):
    print(f" Your love score is {love_score}, you go together . ")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}, you are not meant to be.")

