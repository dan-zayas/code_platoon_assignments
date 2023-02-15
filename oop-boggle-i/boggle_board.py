import random

possible = ["AAEEGN", "ELRTTY", "AOOTTW", "ABBJOO", "EHRTVW", "CIMOTU", "DISTTY", "EIOSST", "DELRVY", "ACHOPS", "HIMNQU", "EEINSU", "EEGHNW", "AFFKPS", "HLNNRZ", "DEILRX "]

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
  
  def get_board(self):
    return self.improved_board
  
  def word_combos(self):

    #delete \n in string
    no_new_lines = ''.join(self.board.splitlines())

    listify_str = list(no_new_lines)
    #eliminate spaces in list
    s = [ele for ele in listify_str if ele.strip()]
    
    valid_words = []
    diag1 = f"{s[0]}{s[5]}{s[10]}{s[15]}"
    diag2 = f"{s[3]}{s[6]}{s[9]}{s[12]}"
    valid_words.append(diag1)
    valid_words.append(diag2)

    i = 15
    while i >= 0:
      if i % 4 == 0:
        horizontal_word = f"{s[i]}{s[i+1]}{s[i+2]}{s[i+3]}"
        horiz_rev = horizontal_word[::-1]
        valid_words.append(horiz_rev)
        valid_words.append(horizontal_word)
      if i < 4:
        vertical_word = f"{s[i]}{s[i+4]}{s[i+8]}{s[i+12]}"
        vert_rev = vertical_word[::-1]
        valid_words.append(vertical_word)
        valid_words.append(vert_rev)
      i -= 1

    self.res = [sub.replace('Q', 'QU') for sub in valid_words]
    
    return self.res
  
  def include_word(self):
    while True:
      submission = input("Try a word")
      if submission.upper() not in self.res:
        print("-------------------------------------")
        print("That is not a valid word")
        print("")
        print(self.improved_board)
        continue
      else:
        print("-------------------------------------")
        print("That is a valid word, you win!")
        break

newBoard = BoggleBoard()
newBoard.shake()
print(newBoard.get_board())
newBoard.word_combos()
newBoard.include_word()