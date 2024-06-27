from itertools import product

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpRequest
from django.views import View
from .forms import UserJobInformationForm, ProductForm, ProductCommentForm
from django.contrib import messages
from .models import Product, ProductPrice
from django.forms import inlineformset_factory, NumberInput
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


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
            return redirect('create_product')
        context = {
            'form': form
        }
        return render(request, 'store/jobandinfo.html', context)


class CreatProductView(LoginRequiredMixin, View):
    """
    this class is for creating and inserting the product into the store database
    """

    def get(self, request: HttpRequest):
        """
        this function is for get method and it's handel the getting method
        """
        ProductPriceFormSet = inlineformset_factory(Product, ProductPrice, fields=('price',), extra=1, widgets={
            'price': NumberInput(attrs={'class': "input is-info", 'style': 'margin:20px'})
        })
        product_form = ProductForm(request.POST, request.FILES)
        price_formset = ProductPriceFormSet()
        context = {
            'product_form': product_form,
            'price_formset': price_formset
        }
        return render(request, 'store/insert-product.html', context)

    def post(self, request: HttpRequest):
        """
        this function is for post method and when post method arrived to this class
        this method will handel it
        """
        ProductPriceFormSet = inlineformset_factory(Product, ProductPrice, fields=('price',), extra=1, widgets={
            'price': NumberInput(attrs={'class': "input is-info", 'style': 'margin:20px'})
        })
        product_form = ProductForm(request.POST, request.FILES)
        price_formset = ProductPriceFormSet(request.POST, instance=product_form.instance)

        if product_form.is_valid() and price_formset.is_valid():
            product = product_form.save()
            price_forms = price_formset.save(commit=False)
            for price_form in price_forms:
                price_form.seller = request.user
                price_form.save()
            messages.success(request, 'The product that you inserted has created successfully.')
            return redirect(reverse_lazy('create_product'))
        context = {
            'product_form': product_form,
            'price_formset': price_formset
        }
        return render(request, 'store/insert-product.html', context)


class ProductListView(LoginRequiredMixin, ListView):
    """
    this class is for showing the list of the all the products that users suggest to others
    and we can read about them and if they were seller we can order it to them...
    """
    model = Product
    template_name = 'store/main_index_store.html'
    context_object_name = 'products'


class ProductDetailView(View):
    """
    showing the detail of the product
    """

    def get(self, request: HttpRequest, slug):
        """
        this function is for showing the detail of the product with slug and it's for handling the get method
        in that
        """
        form = ProductCommentForm()
        product = get_object_or_404(Product, slug=slug)
        context = {
            'product': product,
            'form': form
        }
        return render(request, 'store/product_detail.html', context)

    def post(self, request: HttpRequest, slug):
        """
        this function is for post method and when post method arrived to this class
        """
        form = ProductCommentForm(request.POST)
        product = get_object_or_404(Product, slug=slug)
        if product:
            if form.is_valid():
                comment = form.save(commit=False)
                comment.product = product
                comment.user = request.user
                comment.save()
                messages.success(request, 'The comment was successfully added.')
                return redirect(reverse_lazy('product_detail', args=[slug]))
        else:
            messages.error(request, "this product that you try to submit a message for it , does not exists.")
        context = {
            'product': product,
            'form': form
        }
        return render(request, 'store/product_detail.html', context)
