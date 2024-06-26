
# Przed uruchomieniem
Stworzyć bazę danych w PostmanSQL. Umieścić odpowiedni link do niej w config.py.
Pobrać dependencje za pomocą requirements.py.

Po utworzeniu bazy uruchomić poniższe komendy z poziomu folderu ordersystem/:
```
flask db init
flask db migrate
flask db upgrade
```

# Uruchamianie
UWAGA: przed każdym uruchomieniem/zmianą w envach czy bazie z testowej na zwykłą należy ruszyć
```
source .env
```
Aplikację uruchamiamy za pomocą 
```
flask run
```
z folderu ordersystem/.

# Testowanie
Pilnowanie envów z poprzedniej sekcji dalej ważne.
Do testowania powstał oddzielny skrypt, run_tests.sh, który należy uruchomić z poziomu folderu ordersystem/.

Część unit testów została wykonana w unittest zamiast pytest, a nie zdążyłam ich przemigrować. Aby je uruchomić, należy zmienić nazwę folderu unittest_tests/ na tests/ i uruchomić komendę
```
python3 -m unittest -v
```
z poziomu folderu ponad folderem tests/.


# Przykładowe użycia api

```
POST(/orders/?name=sample name&description=sample description)
```
Powinno zwrócić przykładowo
```
{
    "creation_date": "Tue, 25 Jun 2024 21:29:59 GMT",
    "description": "sample description",
    "id": 17,
    "name": "sample name",
    "status": "New"
}
```
creation_date i id oczywiście zależeć będą od dnia ruszania skryptu i ilości orderów na bazie.

Po instrukcje co wkładać do konkretnych requestów kieruję do docstringów w ordersystem/urls.py.
