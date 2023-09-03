from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')



def about_us(request):
    return render(request,'about.html')




def register(request):
    if request.method == 'POST' :
        print(request.POST)
        user_name=request.POST['name']
        print(user_name)
        password=request.POST['pswrd']
        conf_password=request.POST['conf_pswrd']
        img=request.FILES['filename']
        user_create=Registerform(user_name=user_name)
        user_create.save()
        print('hello')
        print(img)
        # form=form_register(user_name,password,conf_password)
        
        # return redirect('home')
        
    return render(request,'register.html')



def sign_in(request):
    return render(request,'login.html')