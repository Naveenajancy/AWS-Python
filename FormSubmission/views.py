from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from .forms import CustomerForm

def index(request):
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'index.html', context)



