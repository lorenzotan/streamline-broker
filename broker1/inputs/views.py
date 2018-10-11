
# Imports
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
#from .forms import LenderForm, LoanForm, BlocLoanForm
from .forms import *
from django.template import loader
from .models import *



# defs
# XXX ref when adding multiple forms
# https://collingrady.wordpress.com/2008/02/18/editing-multiple-objects-in-django-with-newforms/

# NOTE this needs to match the list in loan_form.html template
LoanTypeForms = {
    'Bloc': BlocLoanForm,
    'Construction': ConstructionLoanForm,
    'Mixed Use': MixedUseLoanForm,
    'Multi Family': MultiFamilyLoanForm,
    'Retail': RetailLoanForm,
}

LoanTypeModels = {
    'Bloc': BlocLoan,
    'Construction': ConstructionLoan,
    'Mixed Use': MixedUseLoan,
    'Multi Family': MultiFamilyLoan,
    'Retail': RetailLoan,
}

# https://stackoverflow.com/questions/3269931/get-model-equivalent-for-modelforms
# TODO load data if it exists
def load_loantype_form(request):
    loantype       = request.GET.get('loantype')
    loan_type_form = LoanTypeForms.get(loantype)(request.POST)
    loantype_tmp   = loader.get_template("inputs/loan_type.html")

    context = {
        'loantype_fields': loan_type_form,
        'loantype': loantype,
    }

    return HttpResponse(loantype_tmp.render(context, request))


def index(request):
    template = loader.get_template('inputs/index.html')
    lenders = Lender.objects.values('lender_first_name', 'lender_last_name', 'lender_company')
    loans   = Loan.objects.values('client_first_name', 'client_last_name', 'loan_amount') #TODO add loan type

    context = {
        'lenders': lenders,
        'loans': loans,
    }
    return HttpResponse(template.render(context, request))



def lender_detail(request, pk):
    template = loader.get_template('inputs/lender_detail.html')
    lender = get_object_or_404(Lender, id=pk)
    context = {
        'lender_data': lender
    }

    return HttpResponse(template.render(context, request))


def edit_lender_form(request, pk):
    # these returns a lender object
    #lender = Lender.objects.get(id=pk)
    lender = get_object_or_404(Lender, id=pk)
    submit = 'Update'

    if request.method == 'POST':
        # this returns a queryset object
        #lender = Lender.filter(id=pk).values()

        form = LenderForm(request.POST, instance=lender)
        # TODO need to create a loan type form lookup here

        if form.is_valid():
            # TODO create and redirect to a details or thank you page
            form.save()
            return redirect('inputs:lender_detail', pk=lender.id)
        else:
            print (form.errors)
    else:
        form = LenderForm(instance=lender)

    # XXX i think i only need to pass the lender id
    return render(request, 'inputs/lender_form.html', {'form': form, 'lender': lender, 'submit': submit })


def lender_form(request):
    tmp = loader.get_template("inputs/lender_form.html")
    submit = 'Submit'

    if request.method == 'POST':
        form = LenderForm(request.POST)

        print ("DEBUG: {}".format(request.POST))

        if form.is_valid():
            form.save()

    else:
        form = LenderForm()

    context = {
        'form': form,
        'submit': submit,
    }

    return HttpResponse(tmp.render(context, request))


def lender_list(request):
    template = loader.get_template('inputs/lender_list.html')
    lender_list = Lender.objects.all()
    context = {
        'lenders': lender_list,
    }
    return HttpResponse(template.render(context, request))




# XXX try using DetailView
def loan_detail(request, pk):
    template       = loader.get_template('inputs/loan_detail.html')
    loan           = get_object_or_404(Loan, id=pk)

    # model obj
    #loantype_model = LoanTypeModels.get(loan.client_loan_type)
    #loantype_data  = get_object_or_404(loantype_model, client_id=pk)
    #loantype       = loantype_model.objects.filter(client_id=pk).values()

    #print ()
    #print ("DEBUG: {}".format(loantype))
    #print ()

    context = {
        'loan_data':       loan,
    #    'loantype':        loan.client_loan_type,
    #    'loantype_fields': loantype_data,
    }

    return HttpResponse(template.render(context, request))


#TODO should delete loan type record if it changes
#XXX possible bug if you change the loan type 
#XXX reload loantype info when loan type drop down value changes back to original value
def edit_loan_form(request, pk):
    loan_data          = get_object_or_404(Loan, id=pk)
    loantype_form_obj  = LoanTypeForms.get(loan_data.client_loan_type)
    loantype_model_obj = LoanTypeModels.get(loan_data.client_loan_type)
    loantype_data      = get_object_or_404(loantype_model_obj, client_id=pk)

    submit = 'Update'

    print ("DEBUG BEFORE {}".format(loantype_form_obj))
    print ()
    if request.method == 'POST':
        # this returns a queryset object
        #lender = Lender.filter(id=pk).values()

        form_html         = LoanForm(request.POST, instance=loan_data)
        loantype          = request.POST.get('client_loan_type')
        loantype_form_obj = LoanTypeForms.get(loantype)#(request.POST)
        loantype_html     = loantype_form_obj(request.POST, instance=loantype_data)

        print ()
        print ("DEBUG {}".format(request.POST))
        print ("DEBUG {}".format(loantype_data))
        print ("DEBUG AFTER {}".format(loantype_form_obj))
        print ()

        if form_html.is_valid() and loantype_html.is_valid():
            form_html.save()
            loantype_html.save()

            return redirect('inputs:loan_list')

        else:
            print (form_html.errors)
            print (loantype_html.errors)

    else:
        form_html = LoanForm(instance=loan_data)
        loantype_html = loantype_form_obj(instance=loantype_data)

    print ("DEBUG {}".format(loantype_html))

    context = {
        'form':            form_html,
        'loantype':        loan_data.client_loan_type,
        'loantype_fields': loantype_html,
        'loan_id':         loan_data.id,
        'submit':          submit,
    }

    return render(request, 'inputs/loan_form.html', context)


def loan_form(request):
    submit = "Submit"

    if request.method == 'POST':
        client        = LoanForm(request.POST)
        loantype      = request.POST.get('client_loan_type')
        loantype_form = LoanTypeForms.get(loantype)(request.POST)

        if client.is_valid() and loantype_form.is_valid():
            new_client   = client.save()
            new_loantype = loantype_form.save(commit=False)

            new_loantype.client_id = new_client.id
            new_loantype.save()

        else:
            print (client.errors)
    else:
        client = LoanForm()
    return render(request, 'inputs/loan_form.html', {'form': client, 'submit': submit })


def loan_list(request):
    template = loader.get_template('inputs/loan_list.html')
    loan_list = Loan.objects.all()
    context = {
        'clients': loan_list,
    }
    return HttpResponse(template.render(context, request))
