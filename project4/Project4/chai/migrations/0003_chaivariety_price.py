# Generated by Django 5.1.1 on 2024-09-16 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0002_chaivariety_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivariety',
            name='price',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
