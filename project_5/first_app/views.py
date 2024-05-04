from django.shortcuts import render
from . forms import ContactForm
from . forms import StudentForm , PasswordValidationForm
# Create your views here.


def index(request):

    data = [
        {
            "userId": 1,
            "id": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        },
        {
            "userId": 1,
            "id": 2,
            "title": "qui est esse",
            "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
        },
        {
            "userId": 1,
            "id": 3,
            "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
            "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
        },
        {
            "userId": 1,
            "id": 4,
            "title": "eum et est occaecati",
            "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
        },
        {
            "userId": 1,
            "id": 5,
            "title": "nesciunt quas odio",
            "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque"
        }
    ]

    return render(request, 'index.html', {'data': data})


def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'about.html', {'name': name, 'email': email, 'select': select})
    else:
        return render(request, 'about.html')

def submit_form(request):
    # return render(request, './first_app/form.html')
    # print(request.POST)
    # if request.method == 'POST':
    #     name = request.POST.get('username')
    #     email = request.POST.get('email')
    #     return render(request, 'form.html', {'name': name, 'email': email})
    
    # return render(request, 'form.html')
    return render(request, 'form.html')


def Djangoform(request):
    # form = ContactFrom(request.POST)
    # if form.is_valid():
    #     print(form.cleaned_data)
    # return render(request, 'django_form.html', {'form': form})
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('first_app/upload/'+ file.name ,'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request, 'django_form.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'django_form.html', {'form': form})


def student_form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'student.html', {'form': form})
    else:
        form = StudentForm()
   
    return render(request, 'student.html', {'form': form})


def PasswordForm(request):
    if request.method == 'POST':
        form = PasswordValidationForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'student.html', {'form': form})
    else:
        form = PasswordValidationForm()
   
    return render(request, 'student.html', {'form': form})