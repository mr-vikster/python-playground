import sys
from chords import chords

userInput = sys.argv[1]

print(f'user asked for {userInput}')

if(userInput in chords):
  print("Your chord is " + chords[userInput])
else:
  print("Chord not found")
