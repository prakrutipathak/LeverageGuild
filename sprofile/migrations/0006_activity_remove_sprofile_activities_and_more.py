# Generated by Django 4.1.5 on 2023-02-04 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprofile', '0005_rename_toefl_score_sprofile_family_income_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='sprofile',
            name='activities',
        ),
        migrations.AddField(
            model_name='sprofile',
            name='activities',
            field=models.ManyToManyField(blank=True, to='sprofile.activity'),
        ),
    ]
