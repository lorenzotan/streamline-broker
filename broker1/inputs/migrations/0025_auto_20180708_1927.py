# Generated by Django 2.0.4 on 2018-07-09 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0024_auto_20180708_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='POC_business',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='POC_cell_phone',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='POC_email',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='POC_name',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='POC_work_phone',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='business_main_phone',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='business_name',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='business_type',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='business_website',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='business_year_established',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='client_company_city',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='client_company_name',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='client_company_state',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='client_company_street_address',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='client_company_zip',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='client_occupation',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='docs_P_and_L',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='docs_appraisal',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='docs_brokers_opinion',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='docs_business_taxes',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='docs_credit_report',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='docs_environmental',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='docs_executive_summary',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='docs_expense_report',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='docs_lease_agreements',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='docs_personal_taxes',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='docs_rent_roll',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='fin_bankruptcy',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='fin_fico',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='fin_monthly_payments',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='fin_owns_home',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='fin_salary',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='fin_short_sale',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='fin_total_debt',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='fin_years_in_business',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='loan_amount',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='loan_dcsr',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='loan_desc',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='loan_to_value',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='loan_type',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='property_address',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='property_value',
        ),
    ]
