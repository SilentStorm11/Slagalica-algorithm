from fractions import Fraction

import itertools

import time


def mesto(l):
    n = len(l)
    for i in range(2**n):
        left = [e for j, e in enumerate(l) if i & 2**j]
        right = [e for j, e in enumerate(l) if not i & 2**j]
        yield left, right

def izraz(l):
    if len(l) == 1:
        yield l[0]
    else:
        for left, right in mesto(l):
            if (not left or not right):
                continue
            for el in izraz(left):
                for er in izraz(right):
                    for operator in '+-*/':
                        if(operator=="*" or operator=="/"):
                            yield  el + operator + er
                        else:
                            yield '(' + el + operator + er + ')'
def run(lista):
    global brojac123
    global kraj
    for x in izraz(lista):
        #print(x)
        if (x[0] == "(" and x[len(x) - 1] == ")"):
            print("pokusaj za " + moj_broj + " JE:", x[1:len(x) - 1])
            brojac123+=1
        else:
            print("pokusaj za " + moj_broj + " JE:", x)
            brojac123+=1
        try:
            if (eval(x + "=="+moj_broj)):
              if(x[0]=="(" and x[len(x)-1]==")"):
                print("REŠENJE ZA "+moj_broj+" JE:", x[1:len(x)-1 ])
              else:    print("REŠENJE ZA "+ moj_broj+ " JE:",x)
              kraj=1
              break
        except ZeroDivisionError:
            print("nulica")
kraj=0
brojevi="25-20-9-6-5-1".split("-")
moj_broj="239"
brojac123=0
start = time.time()
print(start)
for n in range(0, len(brojevi)+1):
  for kombinacija in itertools.combinations(brojevi, n) :
      if not kraj:
         run(list(kombinacija))
if(kraj==0):print("NEMA REŠENJA")
#print(time.time()-start)
#print(brojac123)