# Generated by Django 2.1 on 2022-02-09 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220209_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FileField(max_length=25, upload_to=''),
        ),
    ]
