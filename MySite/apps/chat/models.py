from django.db import models
from django.conf import settings


class Topic(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        blank=False
    )
    slug = models.SlugField(
        max_length=255,
        unique=True
    )
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-is_active', '-created', )

    def __str__(self):
        return self.name


class Message(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE
    )
    text = models.TextField(
        max_length=1024,
        blank=False
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return f"{self.topic} on {self.created.strftime('%m/%d/%Y, %H:%M:%S')}"