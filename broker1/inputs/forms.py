# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 10:07:01 2018

@author: eric
"""
from django import forms
from .models import Lender
from .models import Loan
 
class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
    
    
class LenderForm(forms.ModelForm):
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
                  'misc_HELOC','misc_BLOC','misc_bridge',
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


            
#                  'docs_executive_summary','docs_credit_report',
#                  'docs_personal_taxes','docs_business_taxes',
#                  'docs_P_and_L','docs_expense_report','docs_brokers_opinion','docs_appraisal',
#                  'docs_environmental','docs_rent_roll','docs_lease_agreements',
#                  'business_name','business_main_phone',          
#                  'business_website','business_type','business_year_established',
#                  'property_address','property_value',
                  )
#        widgets = {'loan_desc':forms.Textarea(attrs={'rows':4,'cols':15})}

