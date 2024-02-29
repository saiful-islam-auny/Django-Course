from django.shortcuts import render
import datetime
def home(request):
    d = {'name': 'Auny', 'age': 24, 'list':[1,2,3,4,5], 'bd': datetime.datetime.now(), 'val':"",
        
        'courses': [
        {'code': 100, 'name': 'Python', 'fee':2000},
        {'code': 200, 'name': 'Django', 'fee':3000},
        {'code': 300, 'name': 'Flask', 'fee':4000}
    ]}
    return render(request, 'home.html', d) # d is context 
