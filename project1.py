#1- import random module
import random

#2- create subjects
subjects = [
  "Shahrukh khan",
  "MS Dhoni ",
  "Nirmala sitharaman",
  "A Mumbai Cat",
  "Auto Rikshaw Driver from Delhi"
]

actions = [
  "launches",
  "Dances with",
  "eats",
  "Declares war on",
  "Celebrates"
]

places_or_things = [
  "at Red Fort",
  "in Mumbai local train",
  "a plate of Samosa",
  "During IPL Match",
  "at India Gate"
]

#3- Start the headline generation loop
while True:
  subject = random.choice(subjects)
  action = random.choice(actions)
  places_or_thing = random.choice(places_or_things)

  headline = f"BREAKING NEWS: {subject} {action} {places_or_thing}"
  print("\n"+ headline)

  user_input = input("\n Do you want another headline? (yes/no)").strip()
  if user_input == "no":
    break
#print a Goodbye message

print("\n Thank you for using the Fake News Headline Generator.")