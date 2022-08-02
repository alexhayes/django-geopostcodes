# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geopc', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='locality',
            options={'verbose_name_plural': 'localities', 'verbose_name': 'locality'},
        ),
        migrations.AlterField(
            model_name='locality',
            name='postcode',
            field=models.CharField(db_index=True, verbose_name='postcode', help_text='ZIP/Postal code', max_length=15),
        ),
        migrations.AlterField(
            model_name='locality',
            name='suburb',
            field=models.CharField(verbose_name='suburb', help_text='Locality subdivision', max_length=80),
        ),
    ]
