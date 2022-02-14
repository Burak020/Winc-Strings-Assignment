# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1

scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54
goal_0_1 = str(goal_0)
goal_1_1 = str(goal_1)

scorers = scorer_1 + " " + goal_0_1 +','+ " " + scorer_2 +" " + goal_1_1
print(scorers)

report = f'{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute'

print(report)

# Part 2

player = "Ronald Koeman"

find_first_name = player.find('Ronald')
print(find_first_name)

first_name = player[0:6]
print(first_name)

find_last_name = player.find('Koeman')
print(find_last_name)

last_name = player[7:14]
print(last_name)

last_name_len = len(last_name)
print(last_name_len)

name_short = player[0]+"." + " "+ player[7:14]
print(name_short)

first_name = player[0:6]

first_name_len = len(first_name)
print(first_name_len)

chant_name = first_name + "!" + " "

chant_with_whitespace = chant_name * first_name_len
print(chant_with_whitespace)

chant = chant_with_whitespace.strip(" ")
print(chant)

good_chant = (chant!=" ")
print(good_chant)