from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               related_name='+')
    message = models.TextField()
    photo = models.ImageField(blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Java의 toString
    def __str__(self):
        # return f"Custom Post object ({self.id})"
        return self.message

    class Meta:
        ordering = ['-id']

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메세지 글자수"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # post_id 필드가 생성 된다.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    #post_set = models.ManyToManyField(Post)

    def __str__(self):
        return self.name
