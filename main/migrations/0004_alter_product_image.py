# Generated by Django 4.1.2 on 2022-10-05 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(upload_to='products/'),
        ),
    ]
