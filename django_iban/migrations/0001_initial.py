# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from os.path     import join
from os.path     import dirname
from os.path     import abspath
from django.db   import migrations
from django.db   import connection
from django.conf import settings


def create_iban_type(*args, **kwargs):
    database_backend = settings.DATABASES['default']['ENGINE']
    if database_backend in (
        'django.db.backends.postgresql_psycopg2',
        'django.contrib.gis.db.backends.postgis'
    ):
        cursor    = connection.cursor()
        base_path = dirname(dirname(abspath(__file__)))
        cursor.execute("select * from pg_available_extensions where name = 'plpythonu'")
        if cursor.rowcount == 1:
            with open(join(base_path, 'pg_iban_validator.sql')) as iban_type:
                cursor.execute(iban_type.read())


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.RunPython(create_iban_type),
    ]
