# Generated by Django 3.2.9 on 2021-12-11 02:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_auto_20211211_0723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='profileinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
