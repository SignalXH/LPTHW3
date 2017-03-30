#use argument variable
from sys import argv

#define variable name of argv
script, user_name = argv
#define a prompt variable and give it valaue with ''
prompt = '> '

#print strings.and use string.format method.
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
#defin a new variable and take value from input
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
