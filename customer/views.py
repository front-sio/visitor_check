from django.shortcuts import render, redirect
from .models import Customer
from django.contrib.auth.models import Group
from .forms import receptionist_form, save_customer_form, CustomerForm
from django.http import JsonResponse




def save_customer(request):
    if request.method== "POST":
        form = save_customer_form(request.POST)
        form.username = request.POST.get('username')
        form.password1 = request.POST.get('password1')
        form.password2 = request.POST.get('password2')
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(user = user, display_name = user.username)
            return redirect('customer_dashboard')
    return JsonResponse({})


def customerUpdate(request, pk):
    customer = Customer.objects.get(id = pk)
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        form = form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('admin_customers')
    context = {
        'form': form
    }
    return render(request, 'avocado/customers/update.html', context)


