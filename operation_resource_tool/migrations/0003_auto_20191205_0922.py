# Generated by Django 2.1.5 on 2019-12-05 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_resource_tool', '0002_auto_20191205_0759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='path',
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='pathname',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='pathname'),
        ),
    ]
