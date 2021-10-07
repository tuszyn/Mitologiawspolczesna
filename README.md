# Mitologiawspolczesna
Jest to przykładowy scraper utworzony we frameworku Scrapy, który służy do pobierania artykułów ze strony mitologiawspolczesna.pl
# Instalacja i użytkowanie
Do uruchomienia scrapera jest potrzebny python w wersji 3.6+ oraz biblioteki zawarte w pliku requirements.text <br/>Można je zainstalować przy pomocy poniższych komend.
<br/>Na Windowsie

```
pip install -r requirements.txt
```
Na Linuxie
```
pip3 install -r requirements.txt
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
