from django.db import models

# Create your models here.
LOAN_PURPOSE = (
    ('purch',  'Purchase'),
    ('refi',   'Refinance'),
    ('refurb', 'Refurbish'),
)

class Broker(models.Model):
    first_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    last_name  = models.CharField(max_length=50, default=None, blank=True, null=True)
    address    = models.CharField(max_length=50, default=None, blank=True, null=True)
    city       = models.CharField(max_length=50, default=None, blank=True, null=True)
    state      = models.CharField(max_length=50, default=None, blank=True, null=True)
    zip_code   = models.CharField(max_length=50, default=None, blank=True, null=True)
    work_email = models.EmailField(max_length=50, default=None, blank=True, null=True)
    home_email = models.EmailField(max_length=50, default=None, blank=True, null=True)
    work_phone = models.CharField(max_length=50, default=None, blank=True, null=True)
    home_phone = models.CharField(max_length=50, default=None, blank=True, null=True)

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
        ('None', 'Please Select'),
        ('Bloc', 'Bloc'),
        ('Construction', 'Construction'),
        ('Mixed Use', 'Mixed Use'),
        ('Multi Family', 'Multi Family'),
        ('Retail', 'Retail'),
            #(OO, 'Owner Occupied'),
            #(INV, 'Investment'),
            #(CON, 'Construction'),
            #(SBA, 'SBA'),
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
    client_loan_type      = models.CharField(max_length=15, choices=LOAN_TYPE_CHOICES, default=None)

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
            )
            #(UNK, 'Unk'),

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
    lender_solicitation   = models.IntegerField(default = None, blank = True, null = True)

    # Owner Occupied
    oo_office        = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    oo_warehouse     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    oo_manufacturing = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    oo_medical       = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    oo_mixed_use     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    oo_other         = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )

    # Investment
    inv_office        = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    inv_warehouse     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    inv_manufacturing = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    inv_medical       = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    inv_mixed_use     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    inv_other         = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )

    # Multifamily
    mf_2to4           = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    mf_gt4            = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )

    # Construction
    constr_renovation     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    constr_ground_up_spec = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    constr_commercial     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    constr_residential    = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    constr_inv_with_land  = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    constr_oo_with_land   = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )

    # SBA
    sba_7a            = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    sba_504           = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    sba_CAPline       = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    sba_micro         = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    sba_other         = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )

    # HELOC
    heloc_1_pos     = models.BooleanField()
    heloc_2_pos     = models.BooleanField()

    # BLOC
    bloc_resid_prop = models.BooleanField()
    bloc_stocks     = models.BooleanField()
    bloc_savings    = models.BooleanField()
    bloc_inv_prop   = models.BooleanField()
    bloc_1_pos      = models.BooleanField()
    bloc_2_pos      = models.BooleanField()

    # Bridge
    bridge          = models.BooleanField()

    # Qualifiers
    qual_pays_fees        = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_outside_ca       = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_1031_exchange    = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_lt_500K          = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_lt_1M            = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_equip            = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_non_conform      = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_ground_lease     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_relationship     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_cannabis         = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_io               = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_rev_trust        = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_irrev_trust      = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_foreclosure      = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_single_tenant    = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_bk               = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_entitlements     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_non_profit       = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_cashout_refi     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_non_recourse     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_re_collateral    = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_cross_collateral = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    qual_biz_acq          = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )

    prop_automotive      = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    prop_carwash         = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    prop_entertainment   = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    prop_farm            = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    prop_gas_station     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    prop_hospital        = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    prop_hotel_flag      = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    prop_hotel_nonflag   = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    prop_industrial      = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    prop_marina          = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    prop_medical         = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    prop_mobile_home     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    prop_motel_flag      = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    prop_motel_nonflag   = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    prop_multifamily     = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    prop_office          = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    prop_restaurant      = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    prop_retail          = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    prop_senior_housing  = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    prop_storage         = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )
    prop_student_housing = models.CharField(max_length=3, choices=BOOLEAN_CHOICES, default=None, )

    def __str__(self):
        return "{} {}".format(self.lender_first_name, self.lender_last_name)

#class LoanTypes(models.Model):

#class Qualifiers(models.Model):

#TODO should set client as a foreign key
class BlocLoan(models.Model):
    name           = models.CharField(max_length=50, default='', blank=True, null=True)
    address        = models.CharField(max_length=50, default='', blank=True, null=True)
    annual_receipt = models.CharField(max_length=25, verbose_name="Business Name")
    loan_amt       = models.IntegerField(verbose_name="Loan Amount")
    term           = models.IntegerField(default='', verbose_name="Business Name")
    client         = models.OneToOneField(Loan, on_delete=models.CASCADE, null=True)

    #def get_verbose_name(obj):
    #    return obj._meta.verbose_name


class ConstructionLoan(models.Model):
    property_type = models.CharField(max_length=50, default='', blank=True, null=True)
    address       = models.CharField(max_length=50, default='', blank=True, null=True)
    architect     = models.CharField(max_length=50, default='', blank=True, null=True)
    contractor    = models.CharField(max_length=50, default='', blank=True, null=True)
    bridge        = models.NullBooleanField(default=None)
    land          = models.NullBooleanField(default=None)
    client        = models.OneToOneField(Loan, on_delete=models.CASCADE, null=True)


# XXX property type is supposed to be a drop down, what are the choices??
class MixedUseLoan(models.Model):
    property_type   = models.CharField(max_length=25, default='', blank=True, null=True)
    business_list   = models.CharField(max_length=50, default='', blank=True, null=True)
    annual_rent     = models.IntegerField(blank=True, null=True)
    annual_expense  = models.IntegerField(blank=True, null=True)
    purpose         = models.CharField(max_length=15, choices=LOAN_PURPOSE)
    cash_out        = models.NullBooleanField(default=None)
    client          = models.OneToOneField(Loan, on_delete=models.CASCADE, null=True)


class MultiFamilyLoan(models.Model):
    number_of_units = models.IntegerField()
    year_built      = models.IntegerField()
    annual_rent     = models.IntegerField(blank=True, null=True)
    annual_expense  = models.IntegerField(blank=True, null=True)
    purpose         = models.CharField(max_length=15, choices=LOAN_PURPOSE)
    cash_out        = models.NullBooleanField(default=None)
    client          = models.OneToOneField(Loan, on_delete=models.CASCADE, null=True)


class RetailLoan(models.Model):
    property_type  = models.CharField(max_length=25, default='', blank=True, null=True)
    name           = models.CharField(max_length=25, default='', blank=True, null=True)
    address        = models.CharField(max_length=25, default='', blank=True, null=True)
    annual_rent    = models.IntegerField(blank=True, null=True)
    annual_expense = models.IntegerField(blank=True, null=True)
    purpose        = models.CharField(max_length=15, choices=LOAN_PURPOSE)
    cash_out       = models.NullBooleanField(default=None)
    client         = models.OneToOneField(Loan, on_delete=models.CASCADE, null=True)
