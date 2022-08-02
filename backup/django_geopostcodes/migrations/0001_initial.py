# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('iso', django_countries.fields.CountryField(help_text='ISO 3166-1 Country code', verbose_name='iso', max_length=2, db_index=True)),
                ('country', models.CharField(verbose_name='country', max_length=50, help_text='Country name')),
                ('language', models.CharField(help_text='ISO 639-1 language code', verbose_name='language', max_length=2, db_index=True)),
                ('region1', models.CharField(help_text='Administrative region level 1', verbose_name='region 1', max_length=80, db_index=True)),
                ('region2', models.CharField(help_text='Administrative region level 2', verbose_name='region 2', max_length=80, db_index=True)),
                ('region3', models.CharField(help_text='Administrative region level 3', verbose_name='region 3', max_length=80, db_index=True)),
                ('region4', models.CharField(help_text='Administrative region level 4', verbose_name='region 4', max_length=80, db_index=True)),
                ('locality', models.CharField(help_text='Locality name', verbose_name='locality', max_length=80, db_index=True)),
                ('postcode', models.CharField(help_text='ZIP/Postal code', verbose_name='locality', max_length=15, db_index=True)),
                ('suburb', models.CharField(verbose_name='locality', max_length=80, help_text='Locality subdivision')),
                ('latitude', models.FloatField(verbose_name='latitude', help_text='Latitude coordinates in WGS84')),
                ('longitude', models.FloatField(verbose_name='longitude', help_text='Longitude coordinates in WGS84')),
                ('elevation', models.IntegerField(verbose_name='elevation', help_text='Elevation in meters')),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326, db_index=True)),
                ('iso2', models.CharField(verbose_name='ISO2', max_length=10, help_text='ISO 3166-2 Region code')),
                ('fips', models.CharField(verbose_name='FIPS', max_length=10, help_text='NGA Geopolitical code (formerly FIPS PUB 10-4)')),
                ('nuts', models.CharField(verbose_name='NUTS', max_length=12, help_text='European subdivision code')),
                ('hasc', models.CharField(verbose_name='HASC', max_length=12, help_text='Hierarchical administrative subdivision code')),
                ('stat', models.CharField(verbose_name='STAT', max_length=20, help_text='National statistics/census code')),
                ('timezone', models.CharField(verbose_name='timezone', max_length=30, help_text='Time zone name (Olson)')),
                ('utc', models.CharField(verbose_name='utc', max_length=10, help_text='Coordinated Universal Time')),
                ('dst', models.CharField(verbose_name='dst', max_length=10, help_text='Daylight Saving Time')),
            ],
        ),
    ]
