# AGRO

JEDNOM napravimo novi DJANGO projekt na svojem racunalu, aktiviramo naš Virtual Environment (VENV).
Uzmemo File-ove i datoteke sa GitHub projekta i zaljepimo ih u naš stvoreni projekt (tekst gore) - sve osim VENVa (ako se slucajno nalazi neki na GitHubu).
Bonus! : Bilo bi super kada bi nakon svakog "pip install ..." napravili "pip freeze > requirements.txt" i to pushali na GitHub da sljedeca osoba ne mora tražiti greške u kodu i otkrivati što mu fali.
Svaki sljedeci put kada se želi raditi na kodu, otvori se projekt iz prvog retka ovih uputa i u njega se zaljepi kod sa GitHub-a koji se koristio od početka do sada (Oprez! Vjerovatno je da neće raditi ako se u projekt zaljepi kod koji je pisan naknadno u novom venvu negdje jer novije verzije pythona i dodataka nerijetko imaju drugačiju sintaksu!)


1. JEDNOM stvori novi DJANGO projekt
2. Klonirajmo kod i datoteke sa repositorija na kojima želimo raditi (sve osim venv datoteke)
3. pip installajmo nove dodatke ako postoje
4. Kodirajmo!
5. Ako smo pip installali nešto novo, napravimo "pip freeze > requirements.txt"!
6. Nakon što smo gotovi, pušamo izmjene na GitHub (sve osim venv datoteke)

IZI!

25/2/2019 --UPDATE
dodane weather i crops rute
treba pospajat sve sta imamo sutra obavezno!!!!
