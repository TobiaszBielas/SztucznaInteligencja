<<Uruchomienie>>
py -3 main.py 5 5 3 1 -100 100 -100 100 80 20

<<Parametry>>
ilość epok | A | B | C | xMin | xMax | yMin | yMax | ilość punktów treningowych | ilość punktów testowych

<<Input>>
Czy wylosować nowy zestaw danych? (tak/nie)
nie - odczytanie punktów z plików (ilość danych z poprzedniego zapisu 2 ostatnir parametry są nieważne)
w przeciwnym razie losowanie liczb i nadpisanie plików


<<Odpowiedź na pytanie>>
Wnioski: im większa ilość danych treningowych tym szybciej osiągamy rezultat testów w okolicach 100%,
oraz mamy ‘wyższy próg wejścia’ danych testowych (przy 20 punktach treningowych 20%, a przy 800 punktach 90%).
Gdybyśmy ustawili więcej epok tym lepiej skorygowalibyśmy wagi i osiągnęlibyśmy lepsze wyniki (oczywiście przy 
800 punktach treningowych przy tym zestawie wag i punktów osiągnęliśmy już maksimum).