# Generated by Django 2.0.9 on 2018-10-26 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siccodes', '0002_auto_20181026_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='SicCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('sic_code', models.CharField(max_length=4)),
                ('group_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siccodes.IndustryGroup')),
                ('major_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siccodes.MajorGroup')),
                ('sector_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siccodes.IndustrySector')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
