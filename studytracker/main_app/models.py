from django.db import models
# Import the reverse function
from django.urls import reverse
# Create your models here.
from datetime import date, timedelta

from django.contrib.auth.models import User

HEALS = (
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low')
)
class Toy(models.Model):
    link = models.CharField(max_length=550)
    description = models.TextField()
    def __str__(self):
        return f'{self.color} {self.name}'
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

class Card(models.Model):
    goal = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    hours = models.IntegerField()
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= 1

    def __str__(self):
        return self.goal
    def get_absolute_url(self):
        return reverse('detail', kwargs={'card_id': self.id})

class Feeding(models.Model):
    date = models.DateField('Date')
    focus = models.CharField(
        max_length=1,

        choices=HEALS,

        default=HEALS[0][0]
        )
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    time = models.DurationField(default=timedelta(hours=0, minutes=0, seconds=0))
    def __str__(self):
        return f"{self.get_focus_display()} on {self.date}"
    # def studied_for_today(self):
    #     return self.feeding_set.filter(date=date.today()).count() >= len(HEALS)

    #change default sort 
    class Meta:
        ordering = ['-date']
  