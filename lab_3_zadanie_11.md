

    wyświetl wszystkie obiekty modelu Osoba,
    wyświetl obiekt modelu Osoba z id = 3,
    wyświetl obiekty modelu Osoba, których nazwa rozpoczyna się na wybraną przez Ciebie literę alfabetu (tak, żeby był co najmniej jeden wynik),
    wyświetl unikalną listę drużyn przypisanych dla modeli Osoba,
    wyświetl nazwy drużyn posortowane alfabetycznie malejąco,
    dodaj nową instancję obiektu klasy Osoba



from cwiczenia1.models import Osoba Osoba.objects.all()

<QuerySet [<Osoba: Stefan>, <Osoba: Jan>, <Osoba: Bom>]>

Osoba.objects.filter(id=3)

<QuerySet [<Osoba: Bom>]>

Osoba.objects.filter(imie__startswith="S")

<QuerySet [<Osoba: Stefan>]>

from cwiczenia1.models import Druzyna
Druzyna.objects.all().order_by('-nazwa')

<QuerySet [<Druzyna: vegas>, <Druzyna: mks>, <Druzyna: borusja>]>

Osoba.objects.create(imie="Radek", nazwisko="Nowacki")

<Osoba: Radek> 

