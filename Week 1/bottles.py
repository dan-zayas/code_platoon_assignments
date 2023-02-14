# Write a program that can print the song "99 Bottles of Beer".

def bottles(num) :

  while num > 0 :
    if num == 1:
      bot = "bottle"
      dec = "no more"
    else:
      bot = "bottles"
      dec = num-1
    print(str(num) + " " + bot + " of beer on the wall, " + str(num) + " " + bot + " of beer.\nTake one down and pass it around, " + str(dec) + " bottles of beer on the wall.")
    num -= 1
  
  print("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")


print(bottles(99))


