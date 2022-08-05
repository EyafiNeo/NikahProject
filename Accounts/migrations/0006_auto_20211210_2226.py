# Generated by Django 3.2.9 on 2021-12-10 16:26

import Accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_alter_userprofile_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileinfo',
            old_name='proffession',
            new_name='blood_group',
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='educational_qualification',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=Accounts.models.upload_profile_image),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='marital_status',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='other_info',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='permanent_address_district',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='permanent_address_division',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='present_address_district',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='present_address_division',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='skin_tone',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='workplace',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='yearly_income',
            field=models.CharField(default='', max_length=100),
        ),
    ]
