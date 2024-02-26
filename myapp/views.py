from django.http import HttpResponse
from django.shortcuts import render

import datetime

def home(request):

    isActive = True
    if(request.method=='POST'):
        check = request.POST.get('check')
        print(check)
        if check is None: isActive = False
        else: isActive = True

    date = datetime.datetime.now()
    
    name = "Learning With Joy"
    list_of_programs=[
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime numbers from 1 to 100',
        'WAP to print pascals triangle'
    ]
    student={
        'student_name': "Rahul",
        'student_college': "XYZ",
        'student_city': "MUMBAI"
    }
    print("test function is called from view")
    # return HttpResponse("<h1>Hello this is index page </h1>"+str(date))
    data={
        'date': date,
        'isActive': isActive,
        'name': name,
        'list_of_programs': list_of_programs,
        'student_data': student
    }
    return  render(request, 'home.html', data) #{'current_time': str(date)},

def about(request):
    # return HttpResponse("<h1>This is about page</h1>")
    return render(request,'about.html')
    
# def contact(request):
#     if request.method == "POST":
#         name=request.POST['name']
#         email=request.POST['email']
#         message=request.POST['message']
            
#         return HttpResponse('<h3>Name:{}<br/>Email:{},<br/>Message:{}</h3>'.format(name,email,message))
#     else:
#         return render(request,"contact.html")    

# def contact(request):
#     if request.method=="POST":
#         context={}
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data["subject"]
#             from_email = form.cleaned

def services(request):
    # return HttpResponse("<h1>This is services page</h1>")
    return render(request,'services.html')    
