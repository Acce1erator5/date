from django.db import models


# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.PositiveIntegerField()

    STATUS = (('st', 'учусь'),
              ('wk', 'работаю'),
              ('sd', 'Туплю'),
              ('mn', 'Мамкин миллиардер'),
              ('rf', 'Папин бродяга, мамин симпотяга')
              )

    status = models.CharField(max_length=50, choices=STATUS)
    about_yourself = models.TextField()
    salary = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.surname}"

    def get_absolute_url(self):
        return f"/{self.pk}"
