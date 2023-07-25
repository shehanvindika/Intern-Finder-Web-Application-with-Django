from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Register,Posts
from django.contrib import messages
import smtplib
from email.message import EmailMessage

uName=None
cName=None
email=None
location=None


def home(request):
    return render(request,'Home.html')

def logIn(request):

    if request.method == "POST":
        companyUserName = request.POST['uName']
        print(companyUserName)
        companyPassword1 = request.POST['pass1']
        company = Register.objects.all()

        for x in company:
            print(x.userName)
            if x.userName == companyUserName :
                if x.password1 == companyPassword1 :
                    global uName
                    uName=x.userName
                    return redirect('http://127.0.0.1:8000/profile')
                else:
                    messages.error(request,"Invalid password !!!")
                    return render(request,'Login.html')
        messages.error(request,"Invalid user name!!!")
        return render(request, 'Login.html')
            
    return render(request,'Login.html')

def vacancy(request):
    post = Posts.objects.all()
    position='Select a Position'
    list=[]

    if request.method == "POST" and request.POST['position']!='Select a Position':
        position = request.POST['position']
        for y in post:
            if y.position == position:
                list.append(y)
        context = {
            'Post': list,
            'position':position
        }
        return render(request, 'Vacancies.html', context)
    else:
        context = {
            'Post': post,
            'position': position
        }
        return render(request,'Vacancies.html',context)

def createPost(request):
    if request.method == "POST":
        companyName=request.POST['cName']
        position=request.POST['position']
        requirments = request.POST['requirments']
        email = request.POST['email']
        deadline = request.POST['deadline']
        post=Posts(companyName=companyName,position=position,requirments=requirments,email=email,deadline=deadline)
        post.save()
        return redirect('http://127.0.0.1:8000/profile')
    return render(request,'CreatePost.html')

def register(request):
    if request.method == "POST":
        companyName=request.POST['cName']
        companyEmail=request.POST['cEmail']
        companyLocation = request.POST['cLocation']
        companyUserName = request.POST['uName']
        companyPassword1 = request.POST['pass1']
        companyPassword2 = request.POST['pass2']
        company=Register(companyName=companyName,email=companyEmail,userName=companyUserName,location=companyLocation,password1=companyPassword1,password2=companyPassword2)
        company.save()
        return render(request,'Home.html')
    #else:
        #return redirect("Register")
    return render(request,'Register.html')

def profile(request):
    company=Register.objects.all()
    post=Posts.objects.all()
    list=[]
    global email
    global location
    global cName
    global uName

    for x in company:
        if x.userName==uName:
            email = x.email
            location = x.location
            cName=x.companyName

    for y in post:
        if y.companyName==cName:
           list.append(y)
            
    context={
        'CompanyName':cName,
        'Email':email,
        'Location':location,
        'Post':list
    }
    uName=''
    return render(request,'Profile.html',context)


def sendEmails(request):
    email=None
    pass1=None
    cEmail=None
    position='None'
    subject='Apply to the post of'
    if request.method == "POST":
        email=request.POST['userEmail']
        pass1=request.POST['pass1']
        position = request.POST['jobPosition']
        cEmail = request.POST['cEmail']


    #msg = EmailMessage()
    #msg['subject']=subject+position
    #msg['From'] = email
    #msg['To'] = cEmail
    #msg.set_content('Body')

    #with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    #    smtp.login(email,pass1)
    #    smtp.send_message(msg)

    return render(request,'Apply.html')
