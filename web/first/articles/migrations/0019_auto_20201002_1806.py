# Generated by Django 2.2.16 on 2020-10-02 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0018_auto_20200813_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='singlearticlemodel',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='singlearticlemodel',
            name='text',
            field=models.TextField(),
        ),
    ]
