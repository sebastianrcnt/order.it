# Generated by Django 3.2.11 on 2022-02-07 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220207_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuoption',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/menus/images/'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]