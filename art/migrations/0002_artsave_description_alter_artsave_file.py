# Generated by Django 4.1 on 2023-02-25 09:39

import art.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artsave',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='artsave',
            name='file',
            field=models.FileField(upload_to='templates/static/images', validators=[art.validators.validate_file_extension]),
        ),
    ]
