from __future__ import unicode_literals

import os
from datetime import datetime

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.files.storage import FileSystemStorage

media_storage = FileSystemStorage(location=settings.BASE_DIR, base_url="/media/")


class News(models.Model):
    user = models.ForeignKey(User)
    avatar = models.ImageField(upload_to="news/images/", null=True, blank=True)
    title =  models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return u'%s %s' %(self.user.first_name, self.user.last_name)