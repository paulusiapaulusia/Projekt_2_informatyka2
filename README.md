-----------------PROJEKT INFORMATYKA GEODEZYJNA- PROJEKT NR 2-----------------------
Wtyczka Geodetic Calculations

WYMAGANIA SYSTEMOWE:

system Windows 10 lub 11
program QGIS (w wersji minimum 3.22)
python 3.9
biblioteka qgis.PyQt
biblioteka qgis.core
biblioteka qgis.utils
biblioteka numpy
biblioteka os

FUNKCJE WTYCZKI:
Wtyczka pozwala obliczać różnice wysokości między dwoma punktami, oraz pole powierzchni pomiędzy 3 albo więcej punktów. 

>>>Różnice wysokości
Aby policzyć różnice wysokości, trzeba włączyć warstwę, z ktorej chcemy pobrać punkty. Ważne jest to, aby inne warstwy były wyłączone oraz ich punkty odznaczone. Za pomocą funkcji "Zaznacz obiekty prostokątem lub kliknięciem" oraz klawiszem Shift zaznaczamy dwa interesujące nas punkty. W menu wtyczek wybieramy "Geodetic Calculations". W powstałym okienku wybieramy warstwę, na której jesteśmy i klikamy "Oblicz przewyższenie". Jeśli wszystko wykonaliśmy dobrze, program powinien wyświetlić wartość przewyższenia obok przcisku oraz podać komunikat 'Różnica wysokości między wybranymi punktami została policzona'. Podany wynik wyrażony jest w metrach, z centymetrową dokładnością.

>>>Pole powierzchni
Aby policzyć pole powierzchni, postępujemy podobnie jak przy różnicy wysokości. Włączamy warstwę, na której są intereujące nas punkty (pamiętając o wyłączeniu innych) oraz zaznaczamy 3 (!) albo więcej punktów. W menu wtyczek wybieramy Geodetic Calculations oraz wybieramy obecną warstwę. Klikamy "Oblicz pole powierzchni". Jeśli wszystko zostało wykonane prawidłowo, wynik powinien się wyświetlić przy przycisku oraz program powinien podać nam komunikat "Pole powierzchni między wybranymi punktami wynosi: {pole} ha". Podany wynik wyrażany jest w hektarach, z dokładnością do trzeciego miejsca po przecinku.


BŁĘDY
-jeśli użytkownik przy obliczaniu różnicy wysokości zaznaczy tylko jeden punkt, wyświetli się komunikat: 'Aby policzyć wysokosc wybierz DWA PUNKTY'
-jesli użytkownik nie wybierze aktywnej warstwy, dostanie komunikat: 'Nie wybrano aktywnej warstwy'
-jesli przy obliczaniu pola użytkownik wybierze mniej niż 3 punkty, zostanie wyświetlony komunikat: 'Aby policzyć pole powierzchni wybierz co najmniej TRZY PUNKTY'
- jeśli przy wybieraniu punktów będą włączone inne warstwy, program będzie miał problem z pobieram pożądanych wartości- wtedy wyskoczy nam błąd pobierania wartości "feature"

INSTALOWANIE WTYCZKI
Wtyczkę należy pobrać i umieścić ją w folderze "C:\Users\uzytkownik\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins". Potem należy włączyć program QGIS i załadować wtyczkę.
Najlepiej otworzyć mapę zawierającą niezbędne atrybuty oraz elementy geometrii. Takowe można znaleźć na stronie geoportal.gov.pl


