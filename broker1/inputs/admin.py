from django.contrib import admin
from .models import Lender, Loan
from django.http import HttpResponse

# ... export functions will go here ...
# ... export functions will go here ...
def export_loan_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"Client First Name"),
        smart_str(u"Client Last Name"),
        smart_str(u"Client Street Address"),
        smart_str(u"Client City"),
        smart_str(u"Client State"),
        smart_str(u"Client Zip Code"),
        smart_str(u"Client Work Email"),
        smart_str(u"Client Personal Email"),
        smart_str(u"Client Work Phone"),
        smart_str(u"Client Cell Phone"),
        smart_str(u"Client Using POC"),
        
        smart_str(u"POC Name"),
        smart_str(u"POC Company"),
        smart_str(u"POC Work Phone"),
        smart_str(u"POC Cell Phone"),
        smart_str(u"POC Email"),
        
        smart_str(u"Occupation"),
        smart_str(u"Company Name"),
        smart_str(u"Company Street Address"),
        smart_str(u"Company City"),
        smart_str(u"Company State"),
        smart_str(u"Company Zip"),
        
        smart_str(u"Loan Amount"),
        smart_str(u"Loan To Value"),
        smart_str(u"Loan DSCR"),
        smart_str(u"Loan Description"),
        
        smart_str(u"Business Name"),
        smart_str(u"Business Main Phone"),
        smart_str(u"Business Website"),
        smart_str(u"Business Type"),
        smart_str(u"Year Business Established"),
        
                  

        
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.client_first_name),
            smart_str(obj.client_last_name),
            smart_str(obj.client_street_address),
            smart_str(obj.client_city),
            smart_str(obj.client_state),
            smart_str(obj.client_zip_code),
            smart_str(obj.client_work_email),
            smart_str(obj.client_personal_email),
            smart_str(obj.client_work_phone),
            smart_str(obj.client_cell_phone),
            smart_str(obj.client_using_poc),

            smart_str(obj.POC_name),
            smart_str(obj.POC_business),
            smart_str(obj.POC_work_phone),
            smart_str(obj.POC_cell_phone),
            smart_str(obj.POC_email),

            smart_str(obj.client_occupation),
            smart_str(obj.client_company_name),
            smart_str(obj.client_company_street_address),
            smart_str(obj.client_company_city),
            smart_str(obj.client_company_state),
            smart_str(obj.client_company_zip),

            smart_str(obj.loan_amount),
            smart_str(obj.loan_to_value),
            smart_str(obj.loan_dcsr),
            smart_str(obj.loan_desc),

            smart_str(obj.fin_salary),
            smart_str(obj.fin_years_in_business),
            smart_str(obj.fin_total_debt),
            smart_str(obj.fin_monthly_payments),
            smart_str(obj.fin_fico),
            smart_str(obj.fin_owns_home),
            smart_str(obj.fin_bankruptcy),
            smart_str(obj.fin_short_sale),

            smart_str(obj.property_address),
            smart_str(obj.property_value),
            
            smart_str(obj.docs_executive_summary),
            smart_str(obj.docs_credit_report),
            smart_str(obj.docs_personal_taxes),
            smart_str(obj.docs_business_taxes),
            smart_str(obj.docs_P_and_L),
            smart_str(obj.docs_expense_report),
            smart_str(obj.docs_brokers_opinion),
            smart_str(obj.docs_appraisal),
            smart_str(obj.docs_environmental),
            smart_str(obj.docs_rent_roll),
            smart_str(obj.docs_lease_agreements),
            
            smart_str(obj.business_name),
            smart_str(obj.business_main_phone),
            smart_str(obj.business_website),
            smart_str(obj.business_type),
            smart_str(obj.business_year_established),
            

    
        ])
    return response
export_loan_csv.short_description = u"Export Loan CSV"

class LoanAdmin(admin.ModelAdmin):
    actions = [export_loan_csv]

admin.site.register(Loan, LoanAdmin)

def export_lender_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"Lender First Name"),
        smart_str(u"Lender Last Name"),
        smart_str(u"Lender Company"),
        smart_str(u"Lender Street Address"),
        smart_str(u"Lender City"),
        smart_str(u"Lender State"),
        smart_str(u"Lender Zip Code"),
        smart_str(u"Lender Work Email"),
        smart_str(u"Lender Personal Email"),
        smart_str(u"Lender Work Phone"),
        smart_str(u"Lender Cell Phone"),
        smart_str(u"Lender Solicitation?"),

        smart_str(u"Owner Occ. Office?"),
        smart_str(u"Owner Occ. Warehouse?"),
        smart_str(u"Owner Occ. Manufacturing?"),
        smart_str(u"Owner Occ. Medical?"),
        smart_str(u"Owner Occ. Mixed Use?"),
        smart_str(u"Owner Occ. Other?"),

        smart_str(u"Investment Office?"),
        smart_str(u"Investment Warehouse?"),
        smart_str(u"Investment Manufacturing?"),
        smart_str(u"Investment Medical?"),
        smart_str(u"Investment Mixed Use?"),
        smart_str(u"Investment Other?"),

        smart_str(u"MultiFamily 2 to 4"),
        smart_str(u"MultiFamily more than 4"),

        smart_str(u"Construction Renovation"),
        smart_str(u"Construction Ground Up Spec"),
        smart_str(u"Construction Commercial"),
        smart_str(u"Construction Residential"),
        smart_str(u"Construction Investment with Land"),
        smart_str(u"Construction Owner Occ with Land"),

        smart_str(u"SBA 7a?"),
        smart_str(u"SBA 504?"),
        smart_str(u"SBA CAPline?"),
        smart_str(u"SBA Microloan?"),
        smart_str(u"SBA Other?"),
            
        smart_str(u"HELOC?"),
        smart_str(u"BLOC?"),
        smart_str(u"Bridge?"),

        smart_str(u"Pays Brokers fees?"),
        smart_str(u"Outside CA?"),
        smart_str(u"1031 Exchange"),
        smart_str(u"Less than 500K"),
        smart_str(u"Less than 1M"),
        smart_str(u"Equipment Purchase"),
        smart_str(u"Nonconforming Property"),
        smart_str(u"Ground Lease"),
        smart_str(u"Cannabis"),
        smart_str(u"Interest Only"),
        smart_str(u"Revocable Trust"),
        smart_str(u"Irrevocable Trust"),
        smart_str(u"Foreclosure"),
        smart_str(u"Single Tenant"),
        smart_str(u"Bankruptcy"),
        smart_str(u"Entitlements"),
        smart_str(u"Nonprofit"),
        smart_str(u"Cash out Refi"),
        smart_str(u"Non recourse"),
        smart_str(u"Real Estate Collateral"),
        smart_str(u"Cross Collateral"),
        smart_str(u"Business Acquisitions"),

        smart_str(u"Automotive"),
        smart_str(u"Carwash"),
        smart_str(u"Entertainment"),
        smart_str(u"Farm / Agr,"),
        smart_str(u"Gas Station"),
        smart_str(u"Hospital"),
        smart_str(u"Hotel (Flag)"),
        smart_str(u"Hotel (Non-flag)"),
        smart_str(u"Industrial"),
        smart_str(u"Marina"),
        smart_str(u"Medical"),
        smart_str(u"Mobile Home"),
        smart_str(u"Motel (Flag)"),
        smart_str(u"Motel (Non-flag)"),
        smart_str(u"Office"),
        smart_str(u"Restaurant"),
        smart_str(u"Retail"),
        smart_str(u"Senior Housing"),
        smart_str(u"Storage"),
        smart_str(u"Student Housing"),

    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.lender_first_name),
            smart_str(obj.lender_last_name),
            smart_str(obj.lender_company),
            smart_str(obj.lender_street_address),
            smart_str(obj.lender_city),
            smart_str(obj.lender_state),
            smart_str(obj.lender_zip_code),
            smart_str(obj.lender_work_email),
            smart_str(obj.lender_personal_email),
            smart_str(obj.lender_work_phone),
            smart_str(obj.lender_cell_phone),
            smart_str(obj.lender_solicitation),
            
            smart_str(obj.oo_office),
            smart_str(obj.oo_warehouse),
            smart_str(obj.oo_manufacturing),
            smart_str(obj.oo_medical),
            smart_str(obj.oo_mixed_use),
            smart_str(obj.oo_other),
            
            smart_str(obj.inv_office),
            smart_str(obj.inv_warehouse),
            smart_str(obj.inv_manufacturing),
            smart_str(obj.inv_medical),
            smart_str(obj.inv_mixed_use),
            smart_str(obj.inv_other),
            
            smart_str(obj.mf_2to4),
            smart_str(obj.mf_gt4),

            smart_str(obj.constr_renovation),
            smart_str(obj.constr_ground_up_spec),
            smart_str(obj.constr_commercial),
            smart_str(obj.constr_residential),
            smart_str(obj.constr_inv_with_land),
            smart_str(obj.constr_oo_with_land),

            smart_str(obj.sba_7a),
            smart_str(obj.sba_504),
            smart_str(obj.sba_CAPline),
            smart_str(obj.sba_micro),
            smart_str(obj.sba_other),

            smart_str(obj.misc_HELOC),
            smart_str(obj.misc_BLOC),
            smart_str(obj.misc_bridge),

            smart_str(obj.qual_pays_fees),
            smart_str(obj.qual_outside_ca),
            smart_str(obj.qual_1031_exchange),
            smart_str(obj.qual_lt_500K),
            smart_str(obj.qual_lt_1M),
            smart_str(obj.qual_equip),
            smart_str(obj.qual_non_conform),
            smart_str(obj.qual_ground_lease),
            smart_str(obj.qual_relationship),
            smart_str(obj.qual_cannabis),
            smart_str(obj.qual_io),
            smart_str(obj.qual_rev_trust),
            smart_str(obj.qual_irrev_trust),
            smart_str(obj.qual_foreclosure),
            smart_str(obj.qual_single_tenant),
            smart_str(obj.qual_bk),
            smart_str(obj.qual_entitlements),
            smart_str(obj.qual_non_profit),
            smart_str(obj.qual_cashout_refi),
            smart_str(obj.qual_non_recourse),
            smart_str(obj.qual_re_collateral),
            smart_str(obj.qual_cross_collateral),
            smart_str(obj.qual_biz_acq),

            smart_str(obj.prop_automotive),
            smart_str(obj.prop_carwash),
            smart_str(obj.prop_entertainment),
            smart_str(obj.prop_farm),
            smart_str(obj.prop_gas_station),
            smart_str(obj.prop_hospital),
            smart_str(obj.prop_hotel_flag),
            smart_str(obj.prop_hotel_nonflag),
            smart_str(obj.prop_industrial),
            smart_str(obj.prop_marina),
            smart_str(obj.prop_medical),
            smart_str(obj.prop_mobile_home),
            smart_str(obj.prop_motel_flag),
            smart_str(obj.prop_motel_nonflag),
            smart_str(obj.prop_office),
            smart_str(obj.prop_restaurant),
            smart_str(obj.prop_retail),
            smart_str(obj.prop_senior_housing),
            smart_str(obj.prop_storage),
            smart_str(obj.prop_student_housing),

        ])
    return response
export_lender_csv.short_description = u"Export Lender CSV"
 
class LenderAdmin(admin.ModelAdmin):
    actions = [export_lender_csv]

admin.site.register(Lender, LenderAdmin)
