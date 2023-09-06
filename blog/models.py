from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    body = models.TextField(verbose_name='body')
    image = models.ImageField(verbose_name='image', upload_to='blog/')
    views_count = models.IntegerField(default=0, verbose_name='views count')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')

    def __str__(self):
        return f'{self.title} created: {self.created_at}'

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
