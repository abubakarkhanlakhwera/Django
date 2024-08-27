from django.shortcuts import render, redirect
from .models import Member
from .form import MemberForm
from django.contrib import messages

def home(req):
    all_members = Member.objects.all()
    return render(req, 'home.html', {'all': all_members})

def join(req):
    if req.method == "POST":
        form = MemberForm(req.POST or None)
        if form.is_valid():
            form.save()
            messages.success(req, "Member successfully added!")
            return redirect('home')  # Correct redirect to the view name, not HTML
        else:
            fname = req.POST.get('fname')
            lname = req.POST.get('lname')
            age = req.POST.get('age')
            email = req.POST.get('email')
            passwd = req.POST.get('passwd')
            
            messages.error(req, "There was an error!")  # Changed to messages.error
            
            return render(req, 'join.html', {
                'fname': fname,  #  Removed extra space in key
                'lname': lname,
                'age': age,
                'email': email,
                'passwd': passwd,
            })
    else:
        # For non-POST requests, render the form
        return render(req, 'join.html')
