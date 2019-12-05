from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from datetime import datetime



class SaveFileModel(models.Model):
    id = models.AutoField(_('id'), primary_key=True)

    origin_name = models.CharField(_('nr'), max_length=300, db_index=True, null=True, blank=True)

    type = models.CharField(_('nr'), max_length=300, db_index=True, null=True, blank=True)

    name = models.CharField(_('nr'), max_length=300, db_index=True, null=True, blank=True)

    value = models.CharField(_('nr'), max_length=300, db_index=True, null=True, blank=True)
    class Meta():
        db_table = 'save_file'
        verbose_name = _('save file')
        verbose_name_plural = _('save files')