# Laboratorium 2
## Wstęp 
W ramach laboratorium 2 utworzono projekt zgodny z protokołem TIER i zasadami "tidy data". Przenalizowano w nim dane zebrane przez WHO na temat średniego spożycia różnych rodzajów alkoholu na osobę, w 193 różnych krajach na całym świecie w 2010 roku. <br/> 
## Oryginalne dane
W pliku o ścieżce `../Original Data/drinks.csv` zamieszczono oryginalne dane. Dane te zostały gruntownie opisane w pliku `../Original Data/Metadata/Metadata_guide.md`. <br/> 
## Przetwarzanie danych
W celu przetworzenia danych powstał plik `../Command Files/Procedures.ipynb`, który realizuje podstawowe przetwarzenie danych. Każdy z etapów jest w tym pliku opatrzony stosownym komentarzem. Celem tego skryptu jest: <br/>
- zmiana nazw kolumn na nazwy prezentujące również jednostkę, (tak zmienione dane znajdują się w pliku `../Analysis Data/drinks_with_new_colums_name.csv`),
- wypisanie piętnastu największych konsumentów piwa na świecie w przeliczeniu na jedną osobę, (dane te zawiera plik `../Analysis Data/top_beer_consumers.csv`),
- wypisanie piętnastu największych konsumentów wina na świecie w przeliczeniu na jedną osobę, (dane te zawiera plik `../Analysis Data/top_wine_consumers.csv`),
- wypisanie piętnastu największych konsumentów alkoholi wysokoprocentowych na świecie w przeliczeniu na jedną osobę, (dane te zawiera plik `../Analysis Data/top_spirits_consumers.csv`),
- wypisanie piętnastu największych konsumentów czystego alkoholu na świecie w przeliczeniu na jedną osobę, (dane te zawiera plik `../Analysis Data/top_alkohol_consumers.csv`).
Wszystkie z tych danych zostały zapisane w wymienionych plikach. <br/><br/>
Dodatkową funkcją tego skryptu jest możliwość wyrysowania wykresów słupkowych oraz ich zapisanie w formacie jpg. Znajdują się one również w katalogu `../Analysis Data` oraz są nazwane analogiczne do danych, które wykorzystano przy ich tworzeniu (np. dla danych z pliku  `top_beer_consumers.csv` plik z wykresem nazywa się `top_beer_consumers.jpg` itd.).
## Raport oraz pozostała dokumentacja
Końcowy raport z podstawowego przetworzenia danych wraz z wynikami znajduje się w pliku `../Documents/FinalPaper.ipynb`. Ponadto w katalogu `../Documents` znajduje się również ten sam raport w wersji pdf. Natomiast w pliku `../Documents/DataAppendix.md`znajduje się dodatkowy opis przetwarzanych danych.
