from django.shortcuts import render
from . import views
import datetime

# Create your views here.

def home(request):
    d = {
        'name': 'Shubham',
        'age': 25,
        'List': [1, 2, 3, 4], 'val': ['python', 'is', 'fun'],
        'courses': [
            {
                'id': 1,
                'name': "Python",  # Added comma here
                'fee': 1000  # Added comma here
            },
            {
                'id': 2,
                'name': "Django",  # Added comma here
                'fee': 10000  # Added comma here
            },
            {
                'id': 3,
                'name': "C++",  # Added comma here
                'fee': 5000  # Added comma here
            }
        ],
        
        
        'Date': ['Monday', 'Tuesday', 'Wednesday'],
        'birthday': datetime.datetime.now(),
        'Value': 'ramim',
        
        
    }
    
    return render(request, 'home.html', d)
