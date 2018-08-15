# Generated by Django 2.0.4 on 2018-07-09 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0031_auto_20180708_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='docs_P_and_L',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
        migrations.AddField(
            model_name='loan',
            name='docs_appraisal',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
        migrations.AddField(
            model_name='loan',
            name='docs_brokers_opinion',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
        migrations.AddField(
            model_name='loan',
            name='docs_business_taxes',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
        migrations.AddField(
            model_name='loan',
            name='docs_credit_report',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
        migrations.AddField(
            model_name='loan',
            name='docs_environmental',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
        migrations.AddField(
            model_name='loan',
            name='docs_executive_summary',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
        migrations.AddField(
            model_name='loan',
            name='docs_expense_report',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
        migrations.AddField(
            model_name='loan',
            name='docs_lease_agreements',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
        migrations.AddField(
            model_name='loan',
            name='docs_personal_taxes',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
        migrations.AddField(
            model_name='loan',
            name='docs_rent_roll',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
    ]
