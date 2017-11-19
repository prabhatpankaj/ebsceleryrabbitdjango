# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from usermodel.models import User
 
 
class Post(models.Model):
    author = models.ForeignKey(User)
    created = models.DateTimeField('Created Date', default=timezone.now)
    title = models.CharField('Title', max_length=200)
    content = models.TextField('Content')
    slug = models.SlugField('Slug')
    view_count = models.IntegerField("View Count", default=0)
 
    def __str__(self):
        return '"%s" by %s' % (self.title, self.author)