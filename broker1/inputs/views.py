
# Imports
from django.shortcuts import get_object_or_404, redirect, render
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

    print ("REQUEST METHOD: {}".format(request.method))
    # should really use PUT method and combine with lender_form()
    if request.method == 'POST':
        # this returns a queryset object
        #lender = Lender.filter(id=pk).values()

        form = LenderForm(request.POST, instance=lender)
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
    submit = 'Submit'

    if request.method == 'POST':
        form = LenderForm(request.POST)
        form.save()
    else:
        form = LenderForm()
    return render(request, 'inputs/lender_form.html', {'form': form, 'submit': submit })


def lender_list(request):
    template = loader.get_template('inputs/lender_list.html')
    lender_list = Lender.objects.all()
    context = {
        'lenders': lender_list,
    }
    return HttpResponse(template.render(context, request))




def loan_detail(request, pk):
    template = loader.get_template('inputs/loan_detail.html')
    loan = get_object_or_404(Loan, id=pk)
    context = {
        'loan_data': loan
    }

    return HttpResponse(template.render(context, request))


def edit_loan_form(request, pk):
    loan = get_object_or_404(Loan, id=pk)
    submit = 'Update'

    if request.method == 'POST':
        # this returns a queryset object
        #lender = Lender.filter(id=pk).values()

        form = LoanForm(request.POST, instance=loan)
        if form.is_valid():
            # TODO create and redirect to a details or thank you page
            form.save()
            return redirect('inputs:loan_detail', pk=loan.id)
        else:
            print (form.errors)

    else:
        form = LoanForm(instance=loan)

    # XXX i think i only need to pass the loan id
    return render(request, 'inputs/loan_form.html', {'form': form, 'loan': loan, 'submit': submit })


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
