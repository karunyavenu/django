from django.shortcuts import render


def home(request):
    students = [
        {
            'name': 'Anu',
            'grade': 'A',
            'passed': True
        },
        {
            'name': 'Rahul',
            'grade': 'B',
            'passed': False
        },
        {
            'name': 'Meera',
            'grade': 'A+',
            'passed': True
        }
    ]

    return render(request, 'index.html', {'students': students})