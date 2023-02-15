import random

possible = ["AAEEGN", "ELRTTY", "AOOTTW", "ABBJOO", "EHRTVW", "CIMOTU", "DISTTY", "EIOSST", "DELRVY", "ACHOPS", "HIMNQU", "EEINSU", "EEGHNW", "AFFKPS", "HLNNRZ", "DEILRX"]

class BoggleBoard:
  
  def __init__(self):
    self.rows = 4
    self.columns = 4
    self.board = ""
    
  def shake(self):
    while self.rows > 0:
      while self.columns > 0:
        count = len(possible)-1
        single_die = random.randint(0, count)
        die_face = possible[single_die][random.randrange(0,5)]
        self.board += f"{die_face}"
        self.columns -= 1
        possible.pop(single_die)
      self.board += " \n"
      self.rows -= 1
      self.columns = 4

    self.improved_board = ""
    for char in self.board:
      if char == "Q":
        self.improved_board += "Qu "
      elif char == "\n":
        self.improved_board += char
      else:
        self.improved_board += f"{char}  "

    return self.improved_board

newBoard = BoggleBoard()
print(newBoard.shake())