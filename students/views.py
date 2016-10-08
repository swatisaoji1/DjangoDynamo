from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect
from .forms import StudentForm


# Create your views here.

def home(request):
    if not Student.exists():
        Student.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

    data = Student.scan()
    li = []
    for item in data:
        li.append(item)
    li.sort(key=lambda x: x.last_name)
    return render(request, 'students/home.html', {"data" : li})

def new_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student_id =  form.data['student_id']
            first_name = form.data['first_name']
            last_name = form.data['last_name']
            email = form.data['email']
            address = form.data['address']
            gpa = float(form.data['gpa'])

            Student(student_id=student_id, first_name=first_name,
                    last_name=last_name, email=email, address=address,
                    gpa=gpa).save()
            return HttpResponseRedirect('/home/')

    else:
        form = StudentForm()
    return render(request, 'students/create_student.html', {'form' : form})



def edit_student(request, student_id):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student_id = form.data['student_id']
            first_name = form.data['first_name']
            last_name = form.data['last_name']
            email = form.data['email']
            address = form.data['address']
            gpa = float(form.data['gpa'])

            student = Student.get(student_id)
            student.update_item('first_name', first_name, action="PUT")
            student.update_item('last_name', last_name, action="PUT")
            student.update_item('email', email, action="PUT")
            student.update_item('address', address, action="PUT")
            student.update_item('gpa', gpa, action="PUT")

            return HttpResponseRedirect('/home/')
    else:
        try:
            student = Student.get(hash_key=student_id)

        except student.DoesNotExist:
            print("student does not exist")

        form = StudentForm(initial={'student_id': student.student_id,
                                     'first_name': student.first_name,
                                     'last_name': student.last_name,
                                     'email': student.email,
                                     'address': student.address,
                                     'gpa': student.gpa,
                                     })
    return render(request, 'students/create_student.html', {'form': form})


def delete_student(request, student_id):
    try:
        student = Student.get(student_id)
        student.delete()
    except Student.DoesNotExist:
        print("Meeting does not exist")
    return HttpResponseRedirect('/home/')