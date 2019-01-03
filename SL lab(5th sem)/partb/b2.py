class Sentencereverser:
   vowels=['a','e','i','o','u']
   vowelcount=0
   sentence=""
   reverse=""
   def __init__(self,sentence):
     self.sentence=sentence
     self.reverseSentence()
   def reverseSentence(self):
     self.reverse=" ".join(reversed(self.sentence.split(" ")))
   def getvowelcount(self):
     self.vowelcount=sum(s in self.vowels for s in self.sentence.lower())
     return self.vowelcount
   def getreverse(self):
     return self.reverse
items=[]
for i in range(3):
 sentence=input("enter sentence: ")
 reverse=Sentencereverser(sentence.strip())
 items.append(reverse)
sorteditems=sorted(items,key=lambda item: item.getvowelcount(),reverse=True)
for i  in range(len(sorteditems)):
 print("reversed:",sorteditems[i].getreverse(),"vowelcount: ",sorteditems[i].getvowelcount())
    
