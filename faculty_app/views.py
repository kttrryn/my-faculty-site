from django.shortcuts import render, get_object_or_404
from .models import MainPageInfo, Department, Program, Teacher


def main(request):
    info = MainPageInfo.objects.first()
    context = {  # variable names for html
        'info': info
    }
    return render(request, 'index.html', context)


def program_list(request):
    programs = Program.objects.all()
    context = {
        'programs': programs
    }
    return render(request, 'programs_list.html', context)


def program_detail(request, id):
    program = get_object_or_404(Program, id=id)
    context = {
        'program': program
    }
    return render(request, 'program_detail.html', context)


def department_list(request):
    departments = Department.objects.all()
    context = {
        'departments': departments
    }
    return render(request, 'departments_list.html', context)


def department_detail(request, id):
    department = get_object_or_404(Department, id=id)
    teachers = department.teachers.all()
    context = {
        'department': department,
        'teachers': teachers
    }
    return render(request, 'department_detail.html', context)
