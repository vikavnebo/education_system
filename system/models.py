from datetime import datetime

from django.db import models


class Product(models.Model):
	name = models.CharField('Продукт', max_length=100, unique=True)
	author = models.CharField('Автор', max_length=100)
	price = models.IntegerField('Стоимость')
	release = models.DateTimeField('Дата релиза', default=datetime.now())
	min_users_number = models.IntegerField('Минимум человек в группе')
	max_users_number = models.IntegerField('Максимум человек в группе')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'


class Lesson(models.Model):
	name = models.CharField('Название', max_length=100)
	video_url = models.CharField('Ссылка на видео', max_length=600)
	product_id = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Урок'
		verbose_name_plural = 'Уроки'


class User(models.Model):
	first_name = models.CharField('Имя', max_length=50)
	last_name = models.CharField('Фамилия', max_length=50)
	email = models.CharField('Почта', max_length=100, unique=True)
	products = models.ManyToManyField(Product, verbose_name='Продукты', blank=True)

	def __str__(self):
		return f'{self.last_name} {self.first_name}'

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'


class Group(models.Model):
	name = models.CharField('Название', max_length=50)
	product_id = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
	users = models.ManyToManyField(User, verbose_name="Пользователи", blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Группа'
		verbose_name_plural = 'Группы'
