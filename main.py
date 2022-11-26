from getInput import getInput
from search import finalOutput

guess = getInput()
def finalInput(tup):
  numbers= list(tup[0].keys())
  words=[]
  for all in numbers:
    cellNum = all
    length = tup[0][cellNum]
    words= tup[1][:length]
    del tup[1][:length]
    checkInput(list(words),cellNum)
    

def checkInput(list,cellNum):
  final=[]
  for j in range(len(list)):
   for i in range(len(list)):
    if len(list[i])<len(list[j]):
      temp= list[j]
      list[j]=list[i]
      list[i]=temp
  result = finalOutput(final,cellNum,list)
  if result:
    for suggested in result:
      print(suggested, end=" ")
  else:
    print("\nNo Solution")

finalInput(guess)