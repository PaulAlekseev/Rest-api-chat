from django.contrib import admin
from .models import (
    Topic, Message
)


class MessagesInline(admin.TabularInline):
    model = Message
    extra = 1


class TopicAdmin(admin.ModelAdmin):
    inlines = [MessagesInline, ]
    prepopulated_fields = {'slug': ('name', )}
    list_display = ('name', 'owner', 'created', )
    ordering = ('-created', )


class MessageAdmin(admin.ModelAdmin):
    list_display = ('owner', 'topic', 'created', )
    ordering = ('-created', )


admin.site.register(Topic, TopicAdmin)
admin.site.register(Message, MessageAdmin)
