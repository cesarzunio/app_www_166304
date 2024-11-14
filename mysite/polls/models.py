from django.db import models

MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )


class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):

    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60, default="")
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Stanowisko(models.Model):

    nazwa = models.CharField(max_length=100, blank=False, null=False)
    opis = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nazwa


PLEC_CHOICES = [
        ('K', 'Kobieta'),
        ('M', 'Mężczyzna'),
        ('I', 'Inne')
    ]


class Osoba(models.Model):

    imie = models.CharField(max_length=100, blank=False, null=False)
    nazwisko = models.CharField(max_length=100, blank=False, null=False)
    plec = models.CharField(max_length=1, choices=PLEC_CHOICES, blank=False, null=False)
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE, blank=False, null=False)
    data_dodania = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

    class Meta:
        ordering = ['nazwisko']
