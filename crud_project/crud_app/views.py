from django.shortcuts import render, redirect
from .models import Employee


# Create your views here.

def insert_emp(request):
    if request.method == "POST":
        EmpId = request.POST['EmpId']
        EmpName = request.POST['EmpName']
        EmpGender = request.POST['EmpGender']
        EmpEmail = request.POST['EmpEmail']
        EmpDesignation = request.POST['EmpDesignation']
        data = Employee(EmpId=EmpId, EmpName=EmpName, EmpGender=EmpGender, EmpEmail=EmpEmail,
                        EmpDesignation=EmpDesignation)
        data.save()
        #return redirect('show/')
        return render(request, 'show.html', {'EmpName': EmpName})
    else:
        return render(request, 'insert.html')


def show_emp(request):
    staff = Employee.objects.all()
    return render(request, 'show.html', {'staff': staff})


def edit_emp(request, pk):
    staff = Employee.objects.get(id=pk)
    if request.method == 'POST':
        print(request.POST)
        staff.EmpName = request.POST['EmpName']
        staff.EmpGender = request.POST['EmpGender']
        staff.EmpEmail = request.POST['EmpEmail']
        staff.EmpDesignation = request.POST['EmpDesignation']
        staff.save()
        return redirect('/show')
    context = {
        'staff': staff,
    }

    return render(request, 'edit.html', context)


def delete_emp(request, pk):
    staff = Employee.objects.get(id=pk)
    if request.method == 'POST':
        staff.delete()
        return redirect('/show')
    context = {
        'staff': staff,
    }
    return render(request, 'delete.html', context)


def essai(request):
    return render(request, 'essaie.html')

