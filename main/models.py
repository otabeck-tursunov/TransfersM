from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='clubs/', blank=True, null=True)
    president = models.CharField(max_length=255, blank=True, null=True)
    coach = models.CharField(max_length=255, blank=True, null=True)
    found_date = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True, null=True)
    number = models.PositiveSmallIntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    old_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='old_club')
    new_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='new_club')
    price = models.FloatField()
    price_tft = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player.name} -> {self.old_club.name} -> {self.new_club.name}"
