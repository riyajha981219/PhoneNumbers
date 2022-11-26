

numCode = {0:["o","q","z"],1:["i","j"],2:["a","b","c"],3:["d","e","f"],4:["g","h"],5:["k","l"],6:["m","n"],7:["p","r","s"],8:["t","u","v"],9:["w","x","y"]}

def finalOutput(output,number,words):
  for word in words:
    if not output:
      count = searchWordInNum(number,word)
    else:
      for suggested in output:
        if word not in suggested:
          count = searchWordInNum(number,word)

    if count == len(word):
      output.append(word)    
      del words[words.index(word)]
  return output
        
def searchWordInNum(number,word):
  number = list(number)
  numList = []
  count=0
  for letter in word:
    for num in number:
     numList= numCode[int(num)]
     if letter in numList:
          count+=1
          del number[number.index(num)]
          break
     else:
        continue
  return count