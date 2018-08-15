# Generated by Django 2.0.4 on 2018-07-09 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0021_auto_20180708_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='lender',
            name='constr_commercial',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='constr_ground_up_spec',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='constr_inv_with_land',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='constr_oo_with_land',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='constr_renovation',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='constr_residential',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
    ]
