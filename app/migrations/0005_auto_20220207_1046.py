# Generated by Django 3.2.11 on 2022-02-07 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220207_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='menu_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.menucategory'),
        ),
        migrations.AddField(
            model_name='menucategory',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.restaurant'),
        ),
        migrations.AddField(
            model_name='menuoption',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.menu'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='backgroundImage',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/restaurants/background/'),
        ),
    ]