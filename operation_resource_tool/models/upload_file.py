from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from datetime import datetime


class UploadFile(models.Model):
    id = models.AutoField(_('id'), primary_key=True)

    origin_name = models.CharField(_('origin_name'), max_length=300, db_index=True, null=True, blank=True)

    type = models.CharField(_('type'), max_length=300, db_index=True, null=True, blank=True)

    name = models.CharField(_('name'), max_length=300, null=True, blank=True)

    pathname = models.CharField(_('pathname'), max_length=300, null=True, blank=True)

    created_at = models.DateTimeField(_('created_at'), null=True, db_index=True)
