# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Theme, Thumb, Comment, Video

admin.site.register(Theme)
admin.site.register(Thumb)
admin.site.register(Comment)
admin.site.register(Video)
