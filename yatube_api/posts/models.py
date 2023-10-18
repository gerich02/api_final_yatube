from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
MAX_LENGHT = 25


class Group(models.Model):
    title = models.CharField(
        'Название группы',
        max_length=200
    )
    slug = models.SlugField(
        'Уникальный идентификатор',
        unique=True
    )
    description = models.TextField('Описание')

    def __str__(self):
        return self.title[:MAX_LENGHT]


class Post(models.Model):
    text = models.TextField('Текст поста')
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    image = models.ImageField(
        'Прикрепленное изображение',
        upload_to='posts/',
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группа'
    )

    class Meta:
        default_related_name = 'posts'

    def __str__(self):
        return self.text[:MAX_LENGHT]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Пост'
    )
    text = models.TextField(
        'Текст комментария'
    )
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        default_related_name = 'comments'

    def __str__(self):
        return f'Комментарий {self.author[:MAX_LENGHT]} под постом {self.post}'


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )


















# User = get_user_model()

# MAX_LENGHT = 25

# class Group(models.Model):
#     title = models.CharField(
#         'Название группы',
#         max_length=200
#     )
#     slug = models.SlugField(
#         'Уникальный идентификатор',
#         unique=True
#     )
#     description = models.TextField('Описание')

#     def __str__(self):
#         return self.title[:MAX_LENGHT]



# class Post(models.Model):
#     text = models.TextField()
#     pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
#     author = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name='posts')
#     image = models.ImageField(
#         upload_to='posts/', null=True, blank=True)
#     group = 

#     def __str__(self):
#         return self.text[:MAX_LENGHT]


# class Comment(models.Model):
#     author = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name='comments')
#     post = models.ForeignKey(
#         Post, on_delete=models.CASCADE, related_name='comments')
#     text = models.TextField()
#     created = models.DateTimeField(
#         'Дата добавления', auto_now_add=True, db_index=True)
