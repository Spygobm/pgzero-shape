panagram = input("What text do you want to use: ")
alpabet = {
    "a":0,
    "b":0,
    "c":0,
    "d":0,
    "e":0,
    "f":0,
    "g":0,
    "h":0,
    "j":0,
    "k":0,
    "l":0,
    "m":0,
    "n":0,
    "o":0,
    "p":0,
    "q":0,
    "r":0,
    "s":0,
    "t":0,
    "u":0,
    "v":0,
    "w":0,
    "x":0,
    "y":0,
    "z":0
}
for character in panagram:
   if character in alpabet :
      alpabet[character] += 1 

panagram = True
for value in alpabet.values():
   if value == 0:
      panagram = False
if panagram == True:
   print("This is a panagram")
else:
   print("This is not a panagram")
#The quick brown fox jumps over the lazy dog: This is the most famous pangram