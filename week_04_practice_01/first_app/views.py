from django.shortcuts import render, redirect
from .models import PracticeModel  # Import your PracticeModel

# Create your views here.

# def home(request):
#     if request.method == 'POST':
#         form = PracticeForm(request.POST)
#         if form.is_valid():
#             cleaned_data = form.cleaned_data  # Access cleaned_data from form
#             # Process cleaned_data as needed
#             print(cleaned_data)
#     else:
#         form = PracticeForm()
#     return render(request, 'home.html', {'form': form})







from django.shortcuts import render, redirect
from .forms import PracticeModelForm  # Assuming your form is named PracticeModelForm
from .models import PracticeModel

def about(request):
    if request.method == 'POST':
        form = PracticeModelForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            # Optionally, you can redirect to a success page or do other actions here
            return redirect('success_url')  # Replace 'success_url' with the URL name of your success page
    else:
        form = PracticeModelForm()
    return render(request, 'home.html', {'form': form})
