from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views import View
from .forms import UserJobInformationForm, ProductForm
from django.contrib import messages
from .models import UserJobInformation, Product, ProductPrice
from django.forms import inlineformset_factory


class UserInformationAndJobDetailsView(View):
    def get(self, request: HttpRequest):
        """
        this function is for routing and handling the get method in the class view
        """
        form = UserJobInformationForm()
        context = {
            'form': form
        }
        return render(request, 'store/jobandinfo.html', context)

    def post(self, request: HttpRequest):
        """
        this function is for routing and handling the post method in the class view
        """
        form = UserJobInformationForm(request.POST)
        is_submitted_or_not = request.user.userjobinformation_set.first()
        if is_submitted_or_not.is_submitted:
            messages.warning(request, "You submitted this form in the past...")
            return redirect('dashboard')
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.is_submitted = True
            form.save()
            messages.success(request, "Information's of the job and detail of the location was successfully got.")
            return redirect('insert_product')
        context = {
            'form': form
        }
        return render(request, 'store/jobandinfo.html', context)


def create_product(request: HttpRequest):
    ProductPriceFormSet = inlineformset_factory(Product, ProductPrice, fields=('price',), extra=1)
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES)
        price_formset = ProductPriceFormSet(request.POST, instance=product_form.instance)

        if product_form.is_valid() and price_formset.is_valid():
            product = product_form.save()
            price_formset.instance = product
            price_formset.seller = request.user
            price_formset.save()
            messages.success(request, 'The product that you inserted has created successfully.')
            return HttpResponseRedirect('insert_product')
        context = {
            'product_form': product_form,
            'price_formset': price_formset
        }
        return render(request, 'store/insert-product.html', context)
    else:
        product_form = ProductForm()
        price_formset = ProductPriceFormSet()

    context = {
        'product_form': product_form,
        'price_formset': price_formset
    }
    return render(request, 'store/insert-product.html', context)
