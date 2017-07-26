import itertools
import bisect
import collections
import os


def binsearch(lista, rec, lo=0, hi=None):
    if hi is None:
        hi = len(lista)
    while lo < hi:
        mid = (lo + hi) // 2
        if rec < lista[mid]:
            hi = mid
        else:
            lo = mid + 1
    # print("ayyy lmao ",lista[lo-1])
    if rec == lista[lo - 1]:
        return lista[lo - 1]
    else:
        return 0


# collections._OrderedDictKeysView()
r = {"a": {1: ["5", "3", "4"]}, "d": {3: 4}, "c": {3: 4}, "b": {3: 4}}
r["a"][1].sort()
print("".join(r["a"][1]))
r = sorted(r.items())
print(r)
r = list(r)

f = open("reci", "r",encoding="utf8")
recnik = dict()
print(recnik)
kraj=0


for rec in f:
    pom = list(rec.strip())
    pom.sort()

    if "".join(pom) in recnik:
        recnik["".join(pom)].append(rec.strip())

    else:
        recnik["".join(pom)] =  [rec.strip()]

print(recnik.keys())

print(binsearch([1, 2, 3, 4, 5, 7], 5))
string = "nastesšvožvr"
stringsort = list(string)
stringsort.sort()
#####################################################################
korisnik=list("atmosfera")
korisnik_cpy="".join(korisnik)
korisnik.sort()
if "".join(korisnik) in recnik:
    if korisnik_cpy in recnik["".join(korisnik)]:
        print("IMA TA REC I NOSI",len(korisnik_cpy)*2,"PTS-A")
    else: print("NEMA REC")
#####################################################################


for n in reversed(range(3, len(string) + 1)):
    for kombinacija in itertools.combinations(string, n):
            # print("".join(list(permutacija)))
            kombinacija=list(kombinacija)
            kombinacija.sort()
            if "".join(kombinacija) in recnik:
                # if binsearch(list(sorted(recnik[permutacija[0]])),"".join(stringsort)):

                print("NAJDUZA REČ ZA STRING " + string+ " JE: "  ,
                # recnik[permutacija[0]][binsearch(list(sorted(recnik[permutacija[0]])),"".join(stringsort))][0]
                recnik["".join(kombinacija)][0] )
                exit(1)






