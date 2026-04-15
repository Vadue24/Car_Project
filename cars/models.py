import os

from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Car(models.Model):
    title = models.CharField('Name', max_length=50)
    anons = models.CharField('Description', max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    full_text = models.TextField('About')
    date = models.DateTimeField('Date')
    picture = models.ImageField(upload_to='car_images/', default='car_images/car.jpg')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def get_absolute_url(self):
        return f'/news/{self.id}'

@receiver(pre_delete, sender=Car)
def delete_article_image(sender, instance, **kwargs):
    if instance.picture:
        file_path = instance.picture.path
        if os.path.exists(file_path):
            os.remove(file_path)
