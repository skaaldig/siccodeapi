# Generated by Django 2.0.9 on 2018-11-01 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siccodes', '0005_auto_20181101_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siccode',
            name='sic_code',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]