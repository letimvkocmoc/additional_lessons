from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class DatesModelMixin(models.Model):

    class Meta:
        abstract = True

    created = models.DateTimeField(verbose_name='Дата создания')
    updated = models.DateTimeField(verbose_name='Дата обновления')

    def save(self, *args: object, **kwargs: object) -> object:
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super().save(*args, **kwargs)


class Author(DatesModelMixin):

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Фамилия')
    image = models.ImageField(_('image'), upload_to='users_media', null=True, blank=True)

    def image_(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="150"/></a>'.format(self.image.url))
        else:
            return '(Нет фото)'

    image_.short_description = 'Фото'
    image_.allow_tags = True


class Book(DatesModelMixin):

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    title = models.CharField(max_length=255, blank=True, null=True, unique=True, verbose_name='Название')
    description = models.TextField(max_length=255, blank=True, null=True, verbose_name='Описание')
    page_amount = models.IntegerField(blank=True, null=True, verbose_name='Количество страниц')
    author = models.ForeignKey(Author, verbose_name='Автор', on_delete=models.CASCADE, related_name='books')
    available_amount = models.IntegerField(blank=True, null=True, verbose_name='Доступно в наличии')


class User(AbstractUser):

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'

    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Фамилия')
    is_active = models.BooleanField(verbose_name='Статус', default=True)
    phone_number = PhoneNumberField()
    books_taken = models.ManyToManyField(Book, verbose_name='Книги в использовании')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    updated = models.DateTimeField(verbose_name='Дата обновления профиля')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super().save(*args, **kwargs)

    def can_take_book(self):
        return self.books_taken.count() < 3

    def take_book(self, *args, **kwargs):
        if self.can_take_book():
            if Book.available_amount > 0:
                super().save(*args, **kwargs)
            else:
                raise ValueError('Книги нет в наличии!')
        else:
            raise Exception('Больше 3-ех книг брать нельзя!')
