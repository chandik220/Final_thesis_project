from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

from .models import *
from datetime import date

# Create your views here.

def index(request):
    return render(request, 'index.html')

def all_logins(request):
    return render(request, 'all_logins.html')

def donor_login(request):
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"
    return render(request, 'donor_login.html', locals())

def volunteer_login(request):
    return render(request, 'volunteer_login.html')

def admin_login(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"

        return render(request, 'admin_login.html', locals())

def donor_reg(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        contact = request.POST['contact']
        pwd = request.POST['pwd']
        userpic = request.FILES['userpic']
        address = request.POST['address']

        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            Donor.objects.create(user=user,contact=contact,userpic=userpic,address=address)
            error="no"
        except:
            error="yes"
    return render(request, 'donor_reg.html',locals())

def donor_home(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    return render(request, 'donor_home.html')

def donate_now(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)
    if request.method=="POST":
        donationname = request.POST['donationname']
        donationpic = request.FILES['donationpic']
        collectionloc = request.POST['collectionloc']
        description = request.POST['description']
        try:
            Donation.objects.create(donor=donor,
                                    donationname=donationname,
                                    donationpic=donationpic,
                                    collectionloc=collectionloc,
                                    description=description,
                                    status="pending")
            error="no"
        except:
            error="yes"
    return render(request, 'donate_now.html', locals())


def Logout(request):
    logout(request)
    return redirect('index')

def donation_history(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)
    donation = Donation.objects.filter(donor=donor)
    return render(request, 'donation_history.html', locals())

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')


def pending_donation(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation = Donation.objects.filter(status="pending")
    return render(request, 'pending_donation.html', locals())

def view_donationdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation = Donation.objects.get(id="pid")
    if request.method == "POST":
        status = request.POST['status']
        adminremark = request.POST['adminremark']

        try:
            donation.adminremark = adminremark
            donation.status = status
            donation.updationdate = date.today()
            donation.save()
            error="no"
        except:
            error="yes"

    return render(request, 'view_donationdetail.html', locals())