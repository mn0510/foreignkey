from django.shortcuts import render, redirect
from courseapp.models import Course
from courseapp.models import Student
from django.contrib import messages 

# Create your views here.

def home(request):
    return render(request,'home.html')

def course(request):
    return render(request,'course.html')



def add_course(request):
    if request.method=='POST':
        c=request.POST['cname']
        f=request.POST['cfee']
      
        db=Course(course_name=c,course_fee=f)
        db.save()
        return redirect('course')
    
def add_student(request):
    co = Course.objects.all()
    return render(request,'student.html',{'course':co})

def add_studentdb(request):
    if request.method=='POST':
        student_name=request.POST['name']
        student_address=request.POST['address']
        age=request.POST['age']

        jdate=request.POST['jdate']
        sel=request.POST['sel']
        course1=Course.objects.get(id=sel)
        student=Student(student_name=student_name,student_address=student_address,student_age=age,joining_date=jdate,course=course1)
        student.save()
        messages.success(request,' ADD STUDENT SUCCESFULLY')
        return redirect('show_details')
    
def show_details(request):
    student=Student.objects.all()
    return render(request,'details.html',{'students':student})

def edit(request, pk):
    student=Student.objects.get(id=pk)

    course=Course.objects.all()
    return render(request,'edit.html',{'stud':student,'courses': course})

def edit_details(request, pk):
    if request.method=='POST':
       student=Student.objects.get(id=pk)
       student.student_name=request.POST['name']
       student.student_address=request.POST['address']
       student.student_age=request.POST['age']
       student.joining_date=request.POST['jdate']
       
       sel=request.POST['sel']
       course1=Course.objects.get(id=sel)
       student.course=course1
       student.save()
       return redirect('show_details')
    return redirect('edit')


def delete(request,pk):
 
    em=Student.objects.get(id=pk)
    
    em.delete()
    return redirect('show_details')

def back(request):
    return render(request,'home.html')




