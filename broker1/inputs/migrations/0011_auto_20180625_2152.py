# Generated by Django 2.0.4 on 2018-06-26 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0010_auto_20180625_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='lender',
            name='prop_automotive',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='prop_carwash',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='prop_entertainment',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='prop_farm',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='prop_gas_station',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='prop_hospital',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='prop_hotel_flag',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='prop_hotel_nonflag',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='prop_industrial',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='prop_marina',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='prop_medical',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='prop_mobile_home',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='prop_motel_flag',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='prop_motel_nonflag',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='prop_multifamily',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='prop_office',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='prop_restaurant',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='prop_retail',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='prop_senior_housing',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='prop_storage',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
        migrations.AddField(
            model_name='lender',
            name='prop_student_housing',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unk', 'Unk')], default='Unk', max_length=3),
        ),
    ]
