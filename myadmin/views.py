from django.shortcuts import render,redirect

# Create your views here.
def layout(request):
    context={}
    return render(request,'myadmin/common/layout.html',context)

def dashboard(request):
    context={}
    return render(request,'myadmin/dashboard.html',context)

def common_table(request):
    context={}
    return render(request,'myadmin/common/common_table.html',context)

def common_form(request):
    context={}
    return render(request,'myadmin/common/common_form.html',context)