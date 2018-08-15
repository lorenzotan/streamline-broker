from django.db import models

# Create your models here.
class Loan(models.Model):

    # Boolean Choices
    YES = 'Yes'
    NO  = 'No'
    BOOLEAN_CHOICES = (
            (YES, 'Yes'),
            (NO,  'No'),
            )
    
    # Loan Type Choices
    OO = 'Owner Occupied'
    INV = 'Investment'
    CON = 'Construction'
    SBA = 'SBA'
    LOAN_TYPE_CHOICES = (
            (OO, 'Owner Occupied'),
            (INV, 'Investment'),
            (CON, 'Construction'),
            (SBA, 'SBA'),
            )
    

    # Client Personal Information
    client_first_name     = models.CharField(max_length=200, default = None, blank = True, null = True)
    client_last_name      = models.CharField(max_length=200, default = None, blank = True, null = True)
    client_street_address = models.CharField(max_length=200, default = None, null = True)
    client_city           = models.CharField(max_length=200, default = None, blank = True, null = True)
    client_state          = models.CharField(max_length=200, default = None, blank = True, null = True)
    client_zip_code       = models.IntegerField(default = None, null = True)
    client_work_email     = models.EmailField(max_length=200, default = None, blank = True, null = True)
    client_personal_email = models.EmailField(max_length=200, default = None, blank = True, null = True)
    client_work_phone     = models.IntegerField(default = None, blank = True, null = True)
    client_cell_phone     = models.IntegerField(default = None, blank = True, null = True)
    client_using_poc      = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=NO, )  
    
    # POC Contact Information
    POC_name              = models.CharField(max_length=200, default = None, blank = True, null = True)
    POC_business          = models.CharField(max_length=200, default = None, blank = True, null = True)
    POC_work_phone        = models.IntegerField(default = None, blank = True, null = True)
    POC_cell_phone        = models.IntegerField(default = None, blank = True, null = True)
    POC_email             = models.EmailField(max_length=200, default = None, blank = True, null = True)

    # Client occupation and company information
    client_occupation             = models.CharField(max_length=200, default = None, blank = True, null = True)
    client_company_name           = models.CharField(max_length=200, default = None, blank = True, null = True)
    client_company_street_address = models.CharField(max_length=200, default = None, blank = True, null = True)
    client_company_city           = models.CharField(max_length=200, default = None, blank = True, null = True)
    client_company_state          = models.CharField(max_length=200, default = None, blank = True, null = True)
    client_company_zip            = models.IntegerField(default = None, blank = True, null = True)

    # Loan Information
    loan_amount   = models.IntegerField(default = None, blank = True, null = True)
    loan_to_value = models.IntegerField(default = None, blank = True, null = True)
    loan_dcsr     = models.IntegerField(default = None, blank = True, null = True)
    loan_desc     = models.CharField(max_length=200, default = None, blank = True, null = True)
    
    # Financial Information
    fin_salary            = models.IntegerField(default = None, blank = True, null = True)
    fin_years_in_business = models.IntegerField(default = None, blank = True, null = True)
    fin_total_debt        = models.IntegerField(default = None, blank = True, null = True)
    fin_monthly_payments  = models.IntegerField(default = None, blank = True, null = True)
    fin_fico              = models.IntegerField(default = None, blank = True, null = True)
    fin_owns_home         = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=NO, )  
    fin_bankruptcy        = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=NO, )  
    fin_short_sale        = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=NO, )  

    # Property Information
    property_address = models.CharField(max_length=200, default = None, blank = True, null = True)
    property_value   = models.IntegerField(default = None, blank = True, null = True)

    # Docs (Needs List)
    docs_executive_summary = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=NO, )  
    docs_credit_report     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=NO, )  
    docs_personal_taxes    = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=NO, )  
    docs_business_taxes    = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=NO, )  
    docs_P_and_L           = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=NO, )  
    docs_expense_report    = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=NO, )
    docs_brokers_opinion   = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=NO, )  
    docs_appraisal         = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=NO, )  
    docs_environmental     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=NO, )  
    docs_rent_roll         = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=NO, )  
    docs_lease_agreements  = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=NO, )

    # Commercial Business Information
    business_name             = models.CharField(max_length=200, default = None, blank = True, null = True)
    business_main_phone       = models.CharField(max_length=200, default = None, blank = True, null = True)
    business_website          = models.CharField(max_length=200, default = None, blank = True, null = True)
    business_type             = models.CharField(max_length=200, default = None, blank = True, null = True)
    business_year_established = models.IntegerField(default = None, blank = True, null = True)


    def __str__(self):
        return "{} {}".format(self.client_first_name, self.client_last_name)

# Create your models here.
class Lender(models.Model):
    
    YES = 'Yes'
    NO  = 'No'
    UNK = 'Unk'
    
    BOOLEAN_CHOICES = (
            (YES, 'Yes'),
            (NO,  'No'),
            (UNK, 'Unk'),
            )
    
    # Lender Personal Information
    lender_first_name     = models.CharField(max_length=200, default = None, blank = True, null = True)
    lender_last_name      = models.CharField(max_length=200, default = None, blank = True, null = True)
    lender_company        = models.CharField(max_length=200, default = None, blank = True, null = True)
    lender_street_address = models.CharField(max_length=200, default = None, null = True)
    lender_city           = models.CharField(max_length=200, default = None, blank = True, null = True)
    lender_state          = models.CharField(max_length=200, default = None, blank = True, null = True)
    lender_zip_code       = models.IntegerField(default = None, null = True)
    lender_work_email     = models.EmailField(max_length=200, default = None, blank = True, null = True)
    lender_personal_email = models.EmailField(max_length=200, default = None, blank = True, null = True)
    lender_work_phone     = models.IntegerField(default = None, blank = True, null = True)
    lender_cell_phone     = models.IntegerField(default = None, blank = True, null = True)
    lender_solicitation   = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  

    # Owner Occupied
    oo_office        = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    oo_warehouse     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    oo_manufacturing = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    oo_medical       = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    oo_mixed_use     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    oo_other         = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  

    # Investment
    inv_office        = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    inv_warehouse     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    inv_manufacturing = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    inv_medical       = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    inv_mixed_use     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    inv_other         = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    
    # Multifamily
    mf_2to4           = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    mf_gt4            = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    
    # Construction
    constr_renovation     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    constr_ground_up_spec = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    constr_commercial     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    constr_residential    = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    constr_inv_with_land  = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    constr_oo_with_land   = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    
    # SBA
    sba_7a            = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    sba_504           = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    sba_CAPline       = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    sba_micro         = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    sba_other         = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    
    misc_HELOC        = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    misc_BLOC         = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    misc_bridge       = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  

    qual_pays_fees        = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_outside_ca       = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_1031_exchange    = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_lt_500K          = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_lt_1M            = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_equip            = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_non_conform      = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_ground_lease     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_relationship     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_cannabis         = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_io               = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_rev_trust        = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_irrev_trust      = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_foreclosure      = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_single_tenant    = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_bk               = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_entitlements     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_non_profit       = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_cashout_refi     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_non_recourse     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_re_collateral    = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_cross_collateral = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    qual_biz_acq          = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    
    prop_automotive      = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    prop_carwash         = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    prop_entertainment   = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    prop_farm            = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    prop_gas_station     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    prop_hospital        = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    prop_hotel_flag      = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    prop_hotel_nonflag   = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    prop_industrial      = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    prop_marina          = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    prop_medical         = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    prop_mobile_home     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    prop_motel_flag      = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    prop_motel_nonflag   = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    prop_multifamily     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    prop_office          = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    prop_restaurant      = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    prop_retail          = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    prop_senior_housing  = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    prop_storage         = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  
    prop_student_housing = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=UNK, )  

    def __str__(self):
        return "{} {}".format(self.lender_first_name, self.lender_last_name)
    
    