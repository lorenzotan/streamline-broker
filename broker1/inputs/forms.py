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

        widgets = {
            'lender_solicitation': forms.RadioSelect,
            'oo_office': forms.RadioSelect,
            'oo_warehouse': forms.RadioSelect,
            'oo_manufacturing': forms.RadioSelect,
            'oo_medical': forms.RadioSelect,
            'oo_mixed_use': forms.RadioSelect,
            'oo_other': forms.RadioSelect,
            'inv_office': forms.RadioSelect,
            'inv_warehouse': forms.RadioSelect,
            'inv_manufacturing': forms.RadioSelect,
            'inv_medical': forms.RadioSelect,
            'inv_mixed_use': forms.RadioSelect,
            'inv_other': forms.RadioSelect,
            'mf_2to4': forms.RadioSelect,
            'mf_gt4': forms.RadioSelect,
            'constr_renovation': forms.RadioSelect,
            'constr_ground_up_spec': forms.RadioSelect,
            'constr_commercial': forms.RadioSelect,
            'constr_residential': forms.RadioSelect,
            'constr_inv_with_land': forms.RadioSelect,
            'constr_oo_with_land': forms.RadioSelect,
            'sba_7a': forms.RadioSelect,
            'sba_504': forms.RadioSelect,
            'sba_CAPline': forms.RadioSelect,
            'sba_micro': forms.RadioSelect,
            'sba_other': forms.RadioSelect,
            'misc_HELOC': forms.RadioSelect,
            'misc_BLOC': forms.RadioSelect,
            'misc_bridge': forms.RadioSelect,
            'qual_pays_fees': forms.RadioSelect,
            'qual_outside_ca': forms.RadioSelect,
            'qual_1031_exchange': forms.RadioSelect,
            'qual_lt_500K': forms.RadioSelect,
            'qual_lt_1M': forms.RadioSelect,
            'qual_equip': forms.RadioSelect,
            'qual_non_conform': forms.RadioSelect,
            'qual_ground_lease': forms.RadioSelect,
            'qual_relationship': forms.RadioSelect,
            'qual_cannabis': forms.RadioSelect,
            'qual_io': forms.RadioSelect,
            'qual_rev_trust': forms.RadioSelect,
            'qual_irrev_trust': forms.RadioSelect,
            'qual_foreclosure': forms.RadioSelect,
            'qual_single_tenant': forms.RadioSelect,
            'qual_bk': forms.RadioSelect,
            'qual_entitlements': forms.RadioSelect,
            'qual_non_profit': forms.RadioSelect,
            'qual_cashout_refi': forms.RadioSelect,
            'qual_non_recourse': forms.RadioSelect,
            'qual_re_collateral': forms.RadioSelect,
            'qual_cross_collateral': forms.RadioSelect,
            'qual_biz_acq': forms.RadioSelect,
            'prop_automotive': forms.RadioSelect,
            'prop_carwash': forms.RadioSelect,
            'prop_entertainment': forms.RadioSelect,
            'prop_farm': forms.RadioSelect,
            'prop_gas_station': forms.RadioSelect,
            'prop_hospital': forms.RadioSelect,
            'prop_hotel_flag': forms.RadioSelect,
            'prop_hotel_nonflag': forms.RadioSelect,
            'prop_industrial': forms.RadioSelect,
            'prop_marina': forms.RadioSelect,
            'prop_medical': forms.RadioSelect,
            'prop_mobile_home': forms.RadioSelect,
            'prop_motel_flag': forms.RadioSelect,
            'prop_motel_nonflag': forms.RadioSelect,
            'prop_multifamily': forms.RadioSelect,
            'prop_office': forms.RadioSelect,
            'prop_restaurant': forms.RadioSelect,
            'prop_retail': forms.RadioSelect,
            'prop_senior_housing': forms.RadioSelect,
            'prop_storage': forms.RadioSelect,
            'prop_student_housing': forms.RadioSelect,
        }


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
        )


        widgets = {
            'client_using_poc':       forms.RadioSelect,
            'fin_owns_home':          forms.RadioSelect,
            'fin_bankruptcy':         forms.RadioSelect,
            'fin_short_sale':         forms.RadioSelect,
            'docs_executive_summary': forms.RadioSelect,
            'docs_credit_report':     forms.RadioSelect,
            'docs_personal_taxes':    forms.RadioSelect,
            'docs_business_taxes':    forms.RadioSelect,
            'docs_P_and_L':           forms.RadioSelect,
            'docs_expense_report':    forms.RadioSelect,
            'docs_brokers_opinion':   forms.RadioSelect,
            'docs_appraisal':         forms.RadioSelect,
            'docs_environmental':     forms.RadioSelect,
            'docs_rent_roll':         forms.RadioSelect,
            'docs_lease_agreements':  forms.RadioSelect,
        }
#        widgets = {'loan_desc':forms.Textarea(attrs={'rows':4,'cols':15})}

