# Generated by Django 2.0.6 on 2018-07-14 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorp_app', '0014_merge_20180709_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='reg_staff',
            field=models.CharField(default='pradeep', max_length=50),
            preserve_default=False,
        ),
    ]