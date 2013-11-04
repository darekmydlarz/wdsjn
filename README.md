Wprowadzenie do semantyki języka naturalnego
=====
AGH University of Technology and Science
2013/2014

Uruchomienie
------------
** Parser PAP **
```
#!bash
./parser-pap.py <slowo-bodziec> <plik-do-sparsowania> > <output>
```
np.
```
#!bash
./parser-pap.py niemowlę pap.txt > pap-niemowle.txt
```

** Wyszukanie skojarzeń do notatek **
* Uwaga: wymaga [PLP](https://github.com/agh-glk/plp)

```
#!bash
./notatka-skojarzenia-list.py <bodziec-word> <bodziec-notatki-file> <skojarzenie-file> ...
```
Np.
```
#!bash
./notatka-skojarzenia-list.py niemowlę pap-niemowle.txt niemowle.csv dziecko.csv pielucha.csv placz.csv
```
