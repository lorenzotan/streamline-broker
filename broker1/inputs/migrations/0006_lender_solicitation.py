# Generated by Django 2.0.4 on 2018-06-25 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0005_auto_20180624_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='lender',
            name='solicitation',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('', '')], default='', max_length=3),
        ),
    ]
