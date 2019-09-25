#!python3

'''This program exchanges numbers (eg. 1, 35, 142)
for it's word representation (jeden, trzydzieści pięć, ....)

Date: 20190925
'''

import sys

singles = ('','jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć')
teens = ('dziesięć', 'jedenaście', 'dwanaście', 'trzynaście', 'czternaście', 'piętnaście', 'szesnaście', 'siedemnaście', 'osiemnaście', 'dziewiętnaście')
tens = ('','dziesięć', 'dwadzieścia', 'trzydzieści', 'czterdzieści', 'pięćdziesiąt', 'sześćdziesiąt', 'siedemdziesiąt', 'osiedziedziąt', 'dziewięćdziesiąt')
hundreds = ('','sto', 'dwieście', 'trzysta', 'czterysta', 'pięćset', 'sześćset', 'siedemset', 'osiemset', 'dziewięćset')
thousends = ('','tysiąc', 'dwa tysiące', 'trzy tysiące', 'cztery tysiące', 'pięć tysięcy', 'sześć tysięcy', 'siedem tysięcy', 'osiem tysięcy', 'dziewięć tysięcy')


matrix = (singles, tens, hundreds, thousends, teens)

def printNumbers(numbered):
  # remove empty values and join strings
  numbered = "".join(numbered).split()
  print(" ".join(numbered))

def splitdigits(number):  
	# split to list and convert str to int
	return list(map(int, str(number)))

def hasTens(n):
  # check n has x11...x19
  n = "".join(n)
  return 11 <= int(n) and int(n) <= 19

def getNumber(number):
  #reverse dla tablicy
  splited = splitdigits(int(number))[::-1]
  length = abs(len(splited)-1)
  myslist=[]
  i=length
  while(i >= 0):
    #check has x11...x19
    if( i == 1 and length > 0 and hasTens([str(splited[1]), str(splited[0])])):
      myslist.append(matrix[4][splited[0]]+' ') 
      i -= 1
    else:
      myslist.append(matrix[i][splited[i]]+' ') 
    i -= 1
  return myslist

def whileLoop():
  i = 0
  while(i< 180):
    n = getNumber(i)
    printNumbers(n)
    i += 1
  return

def main():
  number = input("\nPodaj liczbę całkowitą w postaci cyfr: ")
  if (not number.isdigit()):
    print("Podany ciąg znaków nie jest liczbą całkowitą. Zatrzymuję!")
    sys.exit()
  elif (len(number)>4):
    print("Podaj liczbę od 0 do 9999")
  else:
    userNUmber = getNumber(int(number))
    printNumbers(userNUmber)
  
#whileLoop()
#if _name_ =="_main_":
while True:
    main()
