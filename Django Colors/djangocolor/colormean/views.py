from django.shortcuts import render

# Create your views here.

def primarycolor(request):
    return render(request,'colormean/primarycolor.html')

def secondarycolor(request):
    return render(request,'colormean/secondarycolor.html')

def specialcolor(request):
    return render(request,'colormean/specialcolor.html')