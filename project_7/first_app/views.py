from django.shortcuts import render
from first_app.forms import StudentForm

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data  # Access cleaned_data from form
            # Process cleaned_data as needed
            print(cleaned_data)
    else:
        form = StudentForm()
    return render(request, 'home.html', {'form': form})
