'''Write a program which can imitate a Grandma who's hard of hearing and follows these constraints:

If you don't input anything (just hit enter) she responds with WHAT?!

If you ask a question with any lower-case letters, she responds with SPEAK UP, KID!

If you talk to her in all upper-case letters, she responds with NO, NOT SINCE 1946!

The first time you say GOODBYE! she says LEAVING SO SOON?

The second time you say GOODBYE! she says LATER, SKATER! and the program exits.'''

def grandma() : 
  times = 0

  while True:
    talk = input("Talk to Grandma:")

    if len(talk) == 0 :
      print("WHAT?!")
      continue

    if talk.isupper() != True:
      print("SPEAK UP, KID!")
      continue
    elif talk.isupper() == True and talk != "GOODBYE!":
      print("NO, NOT SINCE 1946!")
      continue
    elif talk == "GOODBYE!" and times == 0:
      print("LEAVING SO SOON?")
      times += 1
      continue
    elif talk == "GOODBYE!":
      return "LATER, SKATER!"
 



print(grandma())