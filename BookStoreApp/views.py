from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from BookStoreApp.models import regData,Books
from django.urls import reverse

def RegForm(request):
    if request.method=='POST':
        obj=regData()
        obj.firstname=request.POST.get('fname')
        obj.lastname=request.POST.get('lname')
        obj.college_roll=request.POST.get('cRoll')
        obj.batch=request.POST.get('batch')
        obj.branch=request.POST.get('branch')
        obj.email=request.POST.get('email')
        obj.password=request.POST.get('pass')
        obj.cpassword=request.POST.get('cpass')
        if request.POST.get('pass')==request.POST.get('cpass'):
            obj.save()
            msg="""<script>alert("your registration no is ")</script>"""
            return render(request,'login.html')
            # return HttpResponseRedirect(reverse('loginpage'))
        else:
            return HttpResponse("<script>alert('passwords are not same');</script>")
    else:
        return render(request,'registration.html')

def Loginpage(request):
    if request.method=='POST':
        mail=request.POST.get('email')
        pass1=request.POST.get('pass')
        if regData.objects.filter(email=mail,password=pass1):
            showObj=Books.objects.all()
            return render(request,'books.html',{'rec':showObj})
    else:
        return render(request,'login.html')
def pro(request,Pk):
    b=Books.objects.filter(Isbn=Pk)
    print(b)
    return render(request,'proj.html',{'r':b})
