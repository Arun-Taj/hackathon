from django.shortcuts import render,redirect
from . predictDiseaseModule import predict_disease
from . models import Registerform
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from .csvchecker import csvcheck
import csv
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
        if password==conf_password:
           user_create=Registerform(user_name=user_name,password=password,img=img)
           user_create.save()
           messages.success(request, 'Registration successful. You can now log in.')
           return redirect('register')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
      
        
    return render(request,'register.html')



def sign_in(request):
    if request.method== 'POST':
       username = request.POST["username"]
       password = request.POST["password"]
       user = authenticate(request, username=username, password=password)
       if user is not None:
           login(request, user)
           messages.success(request, 'login successful. You can now log in.')
           return redirect('sign_in')
       
       else:
           messages.success(request, "login un successful. You can't now log in.")
        
    return render(request,'login.html')






def predict(request):
    return render(request,'ai.html')



def manipulate(request):
    result=None
    medicine_name=None
    disease_name=None
    if request.method=='POST':
        symptoms=request.POST['symptoms'].split(',')
        print("splitted",symptoms)
        
        if symptoms[0]!='':
            if not csvcheck(symptoms):
                print("show this erro here")
                context={
                    'error':True
                }
                return render(request,'ai.html',context) 
            print(csvcheck(symptoms))
            result=predict_disease(symptoms)
            medicine_name=result['predicted_medicine'][0]
            disease_name=result['predicted_disease'][0]

    context={
        'medicine_name':medicine_name,
        'disease_name':disease_name
    }
    return render(request,'ai.html',context)






def logout_view(request):
    logout(request)
    return redirect('sign_in')





def add_data(request):
    # Collect data from the form or user input
    if request.method=='POST':
        diseases=request.POST['diseases']
        symptoms=request.POST['symptoms']
        medicine=request.POST['medicine']
        data={
            'diseases':diseases,
            'symptoms':symptoms,
            'medicine':medicine
        }
        csv_file_name = 'medicine.csv'

# Write the data to the CSV file
        with open(csv_file_name, mode='a', newline='') as file:
           writer = csv.writer(file)
           writer.writerow([diseases, symptoms, medicine])

           print(f"Data has been written to {csv_file_name}")
        return redirect('index')
        


    return render(request,'doctor.html')

   

def ask_here(request):
    if request.method == 'POST':
       print('hello world')
    #     print('hello')
    # # Gather user data (replace with your data source)
       symptoms=request.POST['symptoms']
       age=request.POST['age']
       dayselapsed=request.POST['dayselapsed']
       email=request.POST['email']

    
       subject = 'User Data Submission'
       body = f"Your '\nEmail: {email}, symptoms:{symptoms},age:{age},dayselapsed:{dayselapsed}"
       from_email = 'aruntajpuriya1@gmail.com'  # Replace with your email address
       recipient_list = ['bishalmurmu150@gmail.com']  # Replace with the static email address

       email = EmailMessage(subject, body, from_email, recipient_list)
       
       try:
          email.send()
          return HttpResponse("User data sent successfully.")
       except Exception as e:
          return HttpResponse(f"An error occurred: {str(e)}")
    
       

    # 
    else:
       return  render(request,'ask.html')



    


        
   
