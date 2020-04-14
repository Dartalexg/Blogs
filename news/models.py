from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()


class Category(models.Model):
    title=models.CharField("Название", max_length=50)

    class Meta:
        verbose_name="Категория"
        verbose_name_plural="Категории"

    def __str__(self):
        return self.title

class Tag(models.Model):
    title=models.CharField("Тег", max_length=50)

    class Meta:
        verbose_name="Тег"
        verbose_name_plural="Теги"

    def __str__(self):
        return self.title



class News (models.Model):
    user=models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.CASCADE)

    category=models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        null=True)

    titel=models.CharField(
        "Загаловок",
        max_length=50)

    text_prev=models.TextField(
        "Краткое Описание",
        max_length=150)

    text=models.TextField(
        "Текст новости",
        max_length=300)

    tag=models.ManyToManyField(
        Tag, verbose_name="Теги")

    data=models.DateTimeField(
        "Дата создания",
        auto_now_add=True)

    description=models.CharField(
        "Описание",
        max_length=100)

    keywords=models.CharField("Ключевые слова",
        max_length=50)

    class Meta:
        verbose_name="Статья"
        verbose_name_plural="Статьи"

    def __str__(self):
        return self.titel

class Commets(models.Model):
    "коменыт"
    user=models.ForeignKey(
        User,
        verbose_name="Пользователи",
        on_delete=models.CASCADE)

    new=models.ForeignKey(
        News,
        verbose_name="Новость",
        on_delete=models.CASCADE)

    data=models.DateTimeField(
        "Дата добавления",
        auto_now_add=True,
        null=True)

    moder=models.BooleanField("Модерация",
    default=False)

    text=models.TextField(
        "Коментарий",
        max_length=50)

    class Meta:
        verbose_name="Коментарий"
        verbose_name_plural="Коментарии"

    def __str__(self):
        return "{}".format(self.user)
