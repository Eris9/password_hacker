import time
from time import sleep
import random
import os

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"

allLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p" , "q" , "r" , "s", "t" , "u" , "v", "w", "x" , "y" , "z" , "0" ,  "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9", "A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" , "M" , "O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z" , "!" , "@" , "#" , "$" , "%" , "^" , "&" , "*" , "(" , ")" , "_" , "-" , "+" , "=" , "`" , "~" , ";" , ":" , "'" , "<" , ">" , "," , "." , "?" , "[" , "]" , "{" , "}" , "|"]

timepassed = 1

passwordcheck = False

isPasswordNotTrue = True

print(green, "Password hacker by Eris9")

sleep(4)

print(blue, "This program isn't interactive, and is meant to be used idly. \nBasically, you can leave this tab open and do something else, since \nit actually takes a while for the computer to get your password.")

sleep(3)

print(red)

print("Also, this program is in it's early stages, so it doesn't do all letters. \nHere is a list of keys you can use:\n\n\nall letters \nnumbers (With special signs.). \nYou can also use all of the special signs, EXCEPT FOR THE QUOTE WITH 2 LINES. \n\nYou can also only put 4 letters in your password.\n\n")

sleep(2)

print(cyan)

userPassword = str(input("Please enter your password that the machine will guess: "))

print(white)

sleep(3)


letter1 = random.choice(allLetters)
letter2 = random.choice(allLetters)
letter3 = random.choice(allLetters)
letter4 = random.choice(allLetters)

passwordGuess = letter1+letter2+letter3+letter4

while passwordcheck == False:
  if isPasswordNotTrue == True:
    letter1 = random.choice(allLetters)
    letter2 = random.choice(allLetters)
    letter3 = random.choice(allLetters)
    letter4 = random.choice(allLetters)

    theFirstWave = letter1+letter2+letter3+letter4

    while theFirstWave != userPassword:
      letter1 = random.choice(allLetters)
      letter2 = random.choice(allLetters)
      letter3 = random.choice(allLetters)
      letter4 = random.choice(allLetters)

      timepassed += 1

      
      if timepassed == 1000000:
        print(white,"1 Million Passwords Guessed So Far...")

      if timepassed == 10000000:
        print(white,"10 Million Passwords Guessed So Far... this might take a while.")

      if timepassed == 50000000:
        print(white,"Oh wow, 50 million Passwords Guessed So Far... jeez.")

      if timepassed == 100000000:
        print(white, "The Ultimate Number, 100 million passwords. WOW")
      
      
      if letter1+letter2+letter3+letter4 == userPassword:
        passwordcheck = True
        isPasswordNotTrue = False
        break



timelapse = timepassed

sleep(3)

print(magenta)

print(timelapse, "password guessed...")


sleep(4)

print(yellow)


print("Password is" , letter1 + letter2 + letter3 + letter4)
