from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .models import Office
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