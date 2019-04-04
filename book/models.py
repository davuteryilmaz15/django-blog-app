from django.db import models

# Create your models here.
class Book(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE, verbose_name = 'Yazar')
    name = models.CharField(max_length = 80, verbose_name = 'Adı')
    page_count = models.IntegerField(verbose_name='Sayfa Sayısı')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')

    def __str__(self):
        return self.name