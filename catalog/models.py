from django.db import models


# 1 - Модель категории товаров:
# ============================
class Category(models.Model):
    # Свойство модели
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.title)


# 2 - Модель производителя товара
# ============================
class Producer(models.Model):
    # Свойство модели
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.title)


# 3 - Модель самого товара:
# =======================
class Product(models.Model):
    # Свойства модели:
    title = models.CharField(max_length=100)
    about = models.TextField(max_length=256)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.FileField(upload_to='pictures/')
    price = models.FloatField()
    count = models.IntegerField()
