# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 10:07:01 2018

@author: eric
"""
from django import forms
from django.utils.translation import gettext_lazy as gettext
from .models import *

class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)


class BrokerForm(forms.ModelForm):
    class Meta:
        model = Broker
        fields = ('first_name', 'last_name', 'address', 'city', 'state', 'zip_code',
                  'work_email', 'home_email', 'work_phone', 'home_phone')


class LenderForm(forms.ModelForm):
    lender_solicitation = forms.NumberInput(attrs={'size': 3})
    # class Meta tells django what model and fields to use
    class Meta:
        model = Lender
        fields = ('lender_first_name', 'lender_last_name','lender_company','lender_street_address',
                  'lender_city','lender_state','lender_zip_code',
                  'lender_work_email','lender_personal_email','lender_work_phone','lender_cell_phone',
                  'lender_solicitation',
                  'oo_office', 'oo_warehouse', 'oo_manufacturing', 'oo_medical', 'oo_mixed_use', 'oo_other', 
                  'inv_office', 'inv_warehouse', 'inv_manufacturing', 'inv_medical', 'inv_mixed_use', 'inv_other', 
                  'mf_2to4','mf_gt4',
                  'constr_renovation','constr_ground_up_spec','constr_commercial','constr_residential','constr_inv_with_land','constr_oo_with_land',
                  'sba_7a','sba_504','sba_CAPline','sba_micro','sba_other',
                  'heloc_1_pos','heloc_2_pos','bloc_resid_prop','bloc_stocks','bloc_savings','bloc_inv_prop','bloc_1_pos','bloc_2_pos','bridge',
                  'qual_pays_fees','qual_outside_ca','qual_1031_exchange','qual_lt_500K','qual_lt_1M',
                  'qual_equip','qual_non_conform','qual_ground_lease','qual_relationship','qual_cannabis',
                  'qual_io','qual_rev_trust','qual_irrev_trust','qual_foreclosure','qual_single_tenant',
                  'qual_bk','qual_entitlements','qual_non_profit','qual_cashout_refi','qual_non_recourse',
                  'qual_re_collateral','qual_cross_collateral','qual_biz_acq',
                  'prop_automotive','prop_carwash','prop_entertainment','prop_farm','prop_gas_station',
                  'prop_hospital','prop_hotel_flag','prop_hotel_nonflag','prop_industrial',
                  'prop_marina','prop_medical','prop_mobile_home','prop_motel_flag','prop_motel_nonflag',
                  'prop_multifamily','prop_office','prop_restaurant','prop_retail',
                  'prop_senior_housing','prop_storage','prop_student_housing',
        )


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ('client_first_name', 'client_last_name',
                  'client_street_address','client_city','client_state','client_zip_code',
                  'client_work_email','client_personal_email',
                  'client_work_phone','client_cell_phone',
                  'client_using_poc',
                  'client_loan_type',
                  'POC_name','POC_business','POC_work_phone','POC_cell_phone','POC_email',
                  'client_occupation','client_company_name','client_company_street_address',
                  'client_company_city','client_company_state','client_company_zip',
                  'loan_amount','loan_to_value','loan_dcsr','loan_desc',
                  'fin_salary','fin_years_in_business','fin_total_debt','fin_monthly_payments',
                  'fin_fico','fin_owns_home','fin_bankruptcy','fin_short_sale',
                  'property_address','property_value',
                  'docs_executive_summary','docs_credit_report','docs_personal_taxes',
                  'docs_business_taxes','docs_P_and_L','docs_expense_report',
                  'docs_brokers_opinion','docs_appraisal','docs_environmental',
                  'docs_rent_roll','docs_lease_agreements',
                  'business_name','business_main_phone','business_website','business_type','business_year_established',
        )


        widgets = {
            'client_using_poc':       forms.RadioSelect,
        }

        labels = {
            'client_loan_type': gettext('Loan Type')
        }



class BlocLoanForm(forms.ModelForm):
    class Meta:
        model = BlocLoan
        prefix = 'loan_type'

        fields = (
            'name',
            'address',
            'annual_receipt',
            'loan_amt',
            'term',
        )

        labels = {
            'name':           gettext('Business Name'),
            'address':        gettext('Business Address'),
            'annual_receipt': gettext('Annual Receipt'),
            'loan_amt':       gettext('Loan Amount'),
            'term':           gettext('Requested Term'),
        }

class ConstructionLoanForm(forms.ModelForm):
    class Meta:
        model = ConstructionLoan
        prefix = 'loan_type'

        fields = (
            'property_type',
            'address',
            'architect',
            'contractor',
            'bridge',
            'land',
        )

        labels = {
            'property_type': gettext('Property Type'),
            'address':       gettext('Address'),
            'architect':     gettext('Architect Name'),
            'contractor':    gettext('General Contractor Name'),
            'bridge':        gettext('Bridge'),
            'land':          gettext('Land'),
        }

        widgets = {
            'bridge': forms.CheckboxInput,
            'land':forms.CheckboxInput,
        }

class MixedUseLoanForm(forms.ModelForm):
    class Meta:
        model = MixedUseLoan
        prefix = 'loan_type'

        fields = (
            'property_type',
            'business_list',
            'annual_rent',
            'annual_expense',
            'purpose',
            'cash_out',
        )

        labels = {
            'property_type':  gettext('Major Property Type'),
            'business_list':  gettext('List of Businesses'),
            'annual_rent':    gettext('Total Annual Rent'),
            'annual_expense': gettext('Total Annual Expenses'),
            'purpose':        gettext('Purpose'),
            'cash_out':       gettext('Cash Out'),
        }

        widgets = { 'cash_out': forms.CheckboxInput, }

class MultiFamilyLoanForm(forms.ModelForm):
    class Meta:
        model = MultiFamilyLoan
        prefix = 'loan_type'

        fields = (
            'number_of_units',
            'year_built',
            'annual_rent',
            'annual_expense',
            'purpose',
            'cash_out',
        )

        labels = {
            'units':          gettext('Number of Units'),
            'year_built':     gettext('Year Builts'),
            'annual_rent':    gettext('Total Annual Rent'),
            'annual_expense': gettext('Total Annual Expenses'),
            'purpose':        gettext('Purpose'),
            'cash_out':       gettext('Cash Out'),
        }

        widgets = { 'cash_out': forms.CheckboxInput, }

class RetailLoanForm(forms.ModelForm):
    class Meta:
        model = RetailLoan
        prefix = 'loan_type'

        fields = (
            'property_type',
            'name',
            'address',
            'annual_rent',
            'annual_expense',
            'purpose',
            'cash_out',
        )

        labels = {
            'property_type':  gettext('Property Type'),
            'name':           gettext('Business Name'),
            'annual_rent':    gettext('Total Annual Rent'),
            'annual_expense': gettext('Total Annual Expenses'),
            'purpose':        gettext('Purpose'),
            'cash_out':       gettext('Cash Out'),
        }

        widgets = { 'cash_out': forms.CheckboxInput, }
