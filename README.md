Wprowadzenie do semantyki języka naturalnego
=====
AGH University of Technology and Science

2013/2014

Użycie
------------
**Text Parser (text-parser.py)**
* Program, który wyciąga z plików ze wskazanych folderów paragrafy, które zawierają słowo-bodziec.
* Działanie programu ścisle związane ze strukturą plików i katalagów dostarczonych przez prof. Lubaszewskiego.
* NKJP i PAP w UTF-8. NKJP w ISO-8859-2.
* Plik PAP musi być przeniesiony do osobnego folderu.
* z katalogów NKJP brane są pod uwagę pliki `text.xml`
* program korzysta z [PLP](https://github.com/agh-glk/plp)
```
./text-parser.py <słowo-bodziec> <dir-with-files> <prus|nkjp|pap>
```  
np. 
```
./text-parser.py niemowlę /home/dariusz/korpusy/pap/ <pap>
```

**Wyszukanie skojarzeń do notatek (notatka-skojarzenia-list.py)**

*Uwaga: wymaga [PLP](https://github.com/agh-glk/plp)*

```
./notatka-skojarzenia-list.py <bodziec-word> <bodziec-notatki-file> <skojarzenie-file> ...
```
```
./notatka-skojarzenia-list.py niemowlę niemowle_pap.txt niemowle.csv dziecko.csv pielucha.csv placz.csv
```
