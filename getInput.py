import sys
guess=[]
def getInput():
  length=0
  cellNum={}
  for line in sys.stdin:
    if '-1'== line.rstrip():
      break
    else:
      if line.rstrip().isnumeric():
        if len(line.rstrip())>1:
          Num=(line.rstrip()) 
        else:
          length= line.rstrip()
          cellNum[Num]=int(length)
      else:
          for i in length:
            guess.append(line.rstrip())
  return (cellNum,guess)

