# Generated by Django 4.2.7 on 2023-11-18 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_motorbike_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorbike',
            name='price',
            field=models.IntegerField(),
        ),
    ]
