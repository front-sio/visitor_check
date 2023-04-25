from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .models import Office, Receptionist
from customer.forms import receptionist_form
from visitor.models import Visitor
import json
from django.http import JsonResponse
from avocado.decorators import customer_only, allowed_user, office_staff_only

@login_required
@office_staff_only
def offices_view(request):
    office_user= request.user.office
    customer = office_user.company
    return render(request, 'office/dashboard/index.html')

@login_required
@office_staff_only
def office_visitors(request):
    return render(request, 'office/visitors/index.html')



@login_required
@office_staff_only
def office_reception(request):
    receptionist = Receptionist.objects.all()
    context = {
        'receptionists': receptionist
    }
    return render(request, 'office/receptionist/index.html', context)



@login_required
@office_staff_only
def office_reception_add(request):
    return render(request, 'office/receptionist/add.html')


@login_required
@office_staff_only
def office_reception_save(request):
    form = receptionist_form()
    if request.method== "POST":
        form = receptionist_form(request.POST)
        form.username = request.POST.get('username')
        form.first_name = request.POST.get('first_name')
        form.last_name = request.POST.get('last_name')
        form.email = request.POST.get('email')
        form.password1 = request.POST.get('password1')
        form.password2 = request.POST.get('password2')
        customer = request.user.customer
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='receptionist')
            user.groups.add(group)
            Receptionist.objects.create(
            user = user,
            name = user.username,
            customer=customer
            )
            return redirect("office_reception")


@login_required
@office_staff_only
def office_visitors_dashboard_live(request):
    office_obj = request.user.office
    not_signed_out = Visitor.objects.filter(office_visited=office_obj, is_signed_out=False).order_by('-time_in')[:8]
    is_signed_out = Visitor.objects.filter(office_visited=office_obj, is_signed_out=True).order_by('-time_in')[:8]
    return JsonResponse({'not_signed_out_visitors': list(not_signed_out.values()), 'is_signed_out_visitors': list(is_signed_out.values())})


@login_required
@office_staff_only
def office_visitor_live(request):
    office_obj = request.user.office
    queryset = Visitor.objects.filter(office_visited=office_obj).order_by('-time_in')[:6]
    return JsonResponse({'visitors': list(queryset.values())})

@login_required
@office_staff_only
def officeUpdate(request, pk):
    office = Office.objects.get(id = pk)
    form = OfficeUpdateForm(instance=office)
    if request.method == "POST":
        form = form = OfficeUpdateForm(request.POST, instance=office)
        if form.is_valid():
            form.save()
            return redirect('admin_offices')
    context = {
        'form': form
    }
    return render(request, 'office/profile/update.html', context)