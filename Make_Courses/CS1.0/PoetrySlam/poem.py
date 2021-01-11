def get_file_lines(filename):
  for lines in filename:
    print (lines)

lines_list = ["Just a small town girl Livin in a lonely world She took the midnight train goin' anywhere", "Just a city boy Born and raised in south Detroit He took the midnight train goin' anywhere", "A singer in a smoky room A smell of wine and cheap perfume", "For a smile they can share the night It goes on and on, and on, and on", "Strangers waiting Up and down the boulevard Their shadows searching in the night", "Streetlights, people Living just to find emotion Hiding somewhere in the night", "Working hard to get my fill Everybody wants a thrill", "Payin' anything to roll the dice Just one more time", "Some will win, some will lose Some were born to sing the blues", "Oh, the movie never ends It goes on and on, and on, and on", "Strangers waiting up and down the boulevard Their shadows searching in the night", "Streetlights, people Living just to find emotion Hiding somewhere in the night", "Don't stop believin' Hold on to the feelin'", "Streetlights, people Don't stop believin' Hold on", "Streetlights, people Don't stop believin' Hold on to the feelin' Streetlights, people"]

for index, lines in enumerate(lines_list, start=1):
       print(index,lines)

def lines_printed_backwards(lines_list):
   for index in reversed(range(len(lines_list))):
      yield index, lines_list[index]
for index, lines in lines_printed_backwards(lines_list):
   print(index,lines)
   
import random

def lines_printed_random(lines_list):
   for index in random.sample(range(len(lines_list)), len(lines_list)):
       yield index, lines_list[index]
for index, lines in lines_printed_random(lines_list):
   print(index,lines)
   
from random import choice


def lines_printed_custom(lines_list):

  bot_response_one = ["Just a small town girl Livin in a lonely world She took the midnight train goin anywhere" ]
  bot_response_two = ["Just a city boy Born and raised in south Detroit He took the midnight train goin' anywhere"]
  bot_response_three = ["A singer in a smoky room A smell of wine and cheap perfume"]
  bot_response_four = ["For a smile they can share the night It goes on and on, and on, and on"]
  bot_response_five = ["Strangers waiting Up and down the boulevard Their shadows searching in the night"]
  bot_response_six = ["Streetlights, people Living just to find emotion Hiding somewhere in the night"]
  bot_response_seven = [ "Working hard to get my fill Everybody wants a thrill", "Payin' anything to roll the dice Just one more time"]
  bot_response_eight = ["Oh, the movie never ends It goes on and on, and on, and on"]
  bot_response_nine = ["Strangers waiting up and down the boulevard Their shadows searching in the night"]
  bot_response_ten = ["Streetlights, people Living just to find emotion Hiding somewhere in the night"]
  bot_response_eleven = ["Don't stop believin' Hold on to the feelin'"]
  bot_response_twelve = ["Streetlights, people Don't stop believin' Hold on"]
  bot_response_thirteen = ["Streetlights, people Don't stop believin' Hold on to the feelin' Streetlights, people"]
  bot_response_fourteen = ["Hold on to the feelin' Streetlights, people"]
 


  if user_response == "lyric one":
    return choice(bot_response_one)
  elif user_response == "lyric two":
    return choice(bot_response_two)
  elif user_response == "lyric three":
    return choice(bot_response_three)
  elif user_response == "lyric four":
    return choice(bot_response_four)
  elif user_response == "lyric five":
    return choice(bot_response_five)
  elif user_response == "lyric six":
    return choice(bot_response_six)
  elif user_response == "lyric seven":
    return choice(bot_response_seven)
  elif user_response == "lyric eight":
    return choice(bot_response_eight)
  elif user_response == "lyric nine":
    return choice(bot_response_nine)
  elif user_response == "lyric ten":
    return choice(bot_response_ten)
  elif user_response == "lyric eleven":
    return choice(bot_response_eleven)
  elif user_response == "lyric twelve":
    return choice(bot_response_twelve)
  elif user_response == "lyric thirteen":
    return choice(bot_response_thirteen)
  elif user_response == "lyric fourteen":
    return choice(bot_response_fourteen)
  else:
    return "Ummmm,no- Try Again"




print("You obviously need help remembering the lyrics, let me help you.")
print(" Select each line of lyric by typing one of the following 'lyric one','lyric two','lyric three','lyric four','lyric five', 'lyric six','lyric seven','lyric eight','lyric nine','lyric ten','lyric eleven','lyric twelve','lyric thirteen', or 'lyric fourteen'and I will make certain you never sing the wrong words again! ")

user_response = ""

while True:
  user_response = input(" Ready To Sing? Type in which line of lyric you want to me to show? : ")
 
 
  if user_response == 'I know the song.':
    break

 
  bot_response = lines_printed_custom(lines_list)
  print(bot_response)