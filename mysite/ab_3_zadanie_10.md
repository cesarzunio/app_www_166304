>>> from polls.models import Osoba
>>> osoby = Osoba.objects.all()
>>> print(osoby)
<QuerySet [<Osoba: Igrek Iksiński>, <Osoba: Jan Kowalski>, <Osoba: Andrzej Patalon>]>
>>> osoba_3 = Osoba.objects.get(id=3) 
>>> print(osoba_3)
Igrek Iksiński
>>> osoby_p = Osoba.objects.filter(nazwisko__startswith='P')
>>> print(osoby_p)
<QuerySet [<Osoba: Andrzej Patalon>]>
>>> stanowiska = Osoba.objects.values_list('stanowisko', flat=True).distinct()
>>> print(stanowiska)
<QuerySet [3, 2, 1]>
>>> osoba_new = Osoba(imie='Radosław', nazwisko='Sikorski', plec='M', stanowisko_id=2)
>>> osoba_new.save()
