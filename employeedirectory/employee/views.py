from django.shortcuts import render

def home(request):

    employees = [
        {
            'name': 'Anu',
            'job': 'Developer',
            'salary': 30000,
            'full_time': True
        },
        {
            'name': 'Rahul',
            'job': 'Designer',
            'salary': 25000,
            'full_time': False
        },
        {
            'name': 'Meera',
            'job': 'Tester',
            'salary': 28000,
            'full_time': True
        }
    ]

    return render(request, 'index.html', {'employees': employees})