#this is hangman game code
import random
print("=====WELCOME IN OUR HANGMAN GAME=====")
print("_____________________________________")
print("\n")
name=input("Enter your name :")
print(f"Hello {name}!")
print("Choose Game Level")
print("1. | Simple")
print("2. | Medium")
print("3. | Hard")
level=int(input("Enter game level(1,2,3) :"))

if level==1:
    word_list=['house','chair','plant','sun','book','fish','tree','car','star','bird','milk','women','box','coat','cake','fire','ring','ship','nail','rope','seed','yes','zero','quiz','burn','rice','flag','key','water','wind','zoo','zebra','earth','jelly']

elif level==2:
    word_list=['puzzle','garden','jungle','laptop','festival','diamond','window','python','school','planet','bridge','guitar','pirate','blanket','galaxy','airpot','magnet','library','island','doctor','phoenix','blister','velvet','elephant','xenon','yacht','zigzag','zipper','quasar','waffle']

else:
    word_list=['aardvark','chandelier','quarantine','engineering','architect','xenophobia','dandelion','exquisite','grapefruit','ingenious','juxtapose','lighthouse','discombobulate','euphemism','vicissitude','mnemonic','lethargic','whimsical','yellowhammer','wunderkind','quincunx','dishonesty','yaffle','xylopyroggraphy','bellicose','chimerical','esoteric']

word=random.choice(word_list)
sample=[]

for i in range(len(word)):
    sample+='_'
    
print(sample)
life=6

stages=['''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
========
''','''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
========
''','''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
========
''','''
   +---+
   |   |
   O   |
  /|   |
       |
       |
========
''','''
   +---+
   |   |
   O   |
   |   |
       |
       |
========
''','''
   +---+
   |   |
   O   |
       |
       |
       |
========
''','''
   +---+
   |   |
       |
       |
       |
       |
========
''']


while life!=0 and '_' in sample:
    letter = input("Guess Letter :").lower()
    for i in range( len(word) ):
        if word[i] == letter:
            sample[i] = letter
    if letter not in word:
        life -= 1
    print(stages[life])
    print(sample)
    
    print("Remaining Life :",life)

if life == 0 or "_" in sample:
    print("\nYou Lose the game!")
else:
    print("\nYOU WON THE GAME")
print("=====Thanks for playing this Hangman Game=====\n")

    
