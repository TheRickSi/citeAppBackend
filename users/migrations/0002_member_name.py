# Generated by Django 4.2.2 on 2023-06-09 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='name',
            field=models.CharField(default='', max_length=70),
            preserve_default=False,
        ),
    ]
