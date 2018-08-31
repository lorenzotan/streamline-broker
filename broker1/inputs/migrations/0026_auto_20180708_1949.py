# Generated by Django 2.0.4 on 2018-07-09 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0025_auto_20180708_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='POC_business',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='POC_cell_phone',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='POC_email',
            field=models.EmailField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='POC_name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='POC_work_phone',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]