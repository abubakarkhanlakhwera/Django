# Generated by Django 5.1.1 on 2024-09-16 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0004_chaivariety_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaivariety',
            name='discount',
            field=models.IntegerField(default=0, max_length=3),
        ),
    ]
