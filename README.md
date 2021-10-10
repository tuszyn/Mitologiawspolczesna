# Mitologiawspolczesna
Jest to przykładowy scraper utworzony we frameworku Scrapy, który służy do pobierania artykułów ze strony mitologiawspolczesna.pl
# Instalacja i użytkowanie
Do uruchomienia scrapera jest potrzebny python w wersji 3.6+ oraz biblioteki zawarte w pliku requirements.text <br/>Można je zainstalować przy pomocy poniższych komend.
<br/>Na Windowsie

```
pip install -r requirements.txt
```
Na Linuxie należy zainstalować poniższe zależności
```
sudo apt-get install python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev

```
I biblioteki z pliku requirements.txt
```
pip3 install -r requirements.txt
```
Gdyby dalej były problemy z kodowaniem to można po prostu zainstalować scrapiego poprzez
```
pip3 install scrapy
```
Następnie będąc w nowo utworzonym folderze przechodzimy do poziomu katalogu w którym znajduje się plik scrapy.cfg
<br/>Jest to warunek konieczny, żeby uruchomić scrapera.
```
cd mitologiawspolczesna
```

Wynik scrapowania możemy otrzymać w dwóch formatach:
<br/>json
```
scrapy crawl -o nazwa_pliku.json
```
csv
```
scrapy crawl -o nazwa_pliku.csv
```
