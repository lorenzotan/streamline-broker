
# Imports
from django.shortcuts import render
from django.http import HttpResponse
from .forms import LenderForm
from .forms import LoanForm
from django.template import loader
from .models import Lender
from .models import Loan


# defs
def index(request):
    template = loader.get_template('inputs/index.html')
    lenders = Lender.objects.values('lender_first_name', 'lender_last_name', 'lender_company')
    loans   = Loan.objects.values('client_first_name', 'client_last_name', 'loan_amount') #TODO add loan type

    context = {
        'lenders': lenders,
        'loans': loans,
    }
    return HttpResponse(template.render(context, request))


def lender_nav(request):
    template = loader.get_template('inputs/lender_nav.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def lender_form(request):
    if request.method == 'POST':
        form = LenderForm(request.POST)
        form.save()
    else:
        form = LenderForm()
    return render(request, 'inputs/lender_form.html', {'form': form})


def lender_list(request):
    template = loader.get_template('inputs/lender_list.html')
    lender_list = Lender.objects.all()
    context = {
        'lenders': lender_list,
    }
    return HttpResponse(template.render(context, request))



def loan_nav(request):
    template = loader.get_template('inputs/loan_nav.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def loan_form(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print (form.errors)
    else:
        form = LoanForm()
    return render(request, 'inputs/loan_form.html', {'form': form})


def loan_list(request):
    template = loader.get_template('inputs/loan_list.html')
    loan_list = Loan.objects.all()
    context = {
        'clients': loan_list,
    }
    return HttpResponse(template.render(context, request))
