# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=255)

    @property
    def theme_score(self):
        score = 0
        for video in self.video_set.all():
            days_since_upload = datetime.now().date() - video.date_uploaded
            time_factor = max(0, 1 - (days_since_upload.days / 365))
            positivity_factor = 0.7 * video.good_comments + 0.3 * video.thumbs_up
            score += video.views * time_factor * positivity_factor
        return score

    def __unicode__(self):
        s = u'%s' % (self.name)
        return s

    def __str__(self):
        s = u'%s' % (self.name)
        return s


class Thumb(models.Model):
    is_positive = models.BooleanField(default=False)
    time = models.DateTimeField()
    video = models.ForeignKey(
        'main.Video', related_name="video_thumb", on_delete=models.CASCADE, null=True, blank=True)


class Comment(models.Model):
    is_positive = models.BooleanField(default=False)
    time = models.DateTimeField()
    video = models.ForeignKey(
        'main.Video', related_name="video_comment", on_delete=models.CASCADE, null=True, blank=True)


class Video(models.Model):
    title = models.CharField(max_length=255)
    date_uploaded = models.DateField()
    views = models.IntegerField()
    themes = models.ManyToManyField(Theme)

    @property
    def good_comments(self):
        positive_comments = 0
        negative_comments = 0
        if len(self.video_comment.all()):
            for comment in self.video_comment.all():
                if comment.is_positive:
                    positive_comments += 1
                else:
                    negative_comments += 1

            return positive_comments / (positive_comments + negative_comments)
        else:
            return 0

    @property
    def thumbs_up(self):
        thumb_up = 0
        thumb_down = 0
        if len(self.video_thumb.all()):
            for thumb in self.video_thumb.all():
                if thumb.is_positive:
                    thumb_up += 1
                else:
                    thumb_down += 1

            return thumb_up / (thumb_up + thumb_down)
        else:
            return 0

    def __unicode__(self):
        s = u'%s' % (self.title)
        return s

    def __str__(self):
        s = u'%s' % (self.title)
        return s
