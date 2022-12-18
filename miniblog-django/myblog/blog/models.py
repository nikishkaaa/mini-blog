from django.db import models

class Post(models.Model):
    """data about post"""
    title = models.CharField('main field', max_length=100)
    description = models.TextField("post's field")
    author = models.CharField("author's name", max_length=100)
    date = models.DateField("date")
    img = models.ImageField('Image', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Comments(models.Model):
    """comments"""
    email = models.EmailField()
    name = models.CharField('name', max_length=50)
    text_comments = models.TextField('text of comments', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Comments'
        verbose_name_plural = 'Comments'