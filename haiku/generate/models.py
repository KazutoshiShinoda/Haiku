# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Generation(models.Model):
    created = models.CharField(max_length=100, blank=True, default='')
