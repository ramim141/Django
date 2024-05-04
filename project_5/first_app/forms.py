from django import forms
from django.core import validators


class ContactForm(forms.Form):
    # name = forms.CharField(label="Username")
    # name = forms.CharField(label="Username:", initial='Ramim', help_text='Total length must be 70 character')
    name = forms.CharField(label="Username:", help_text='Total length must be 70 character', required=False,
                           disabled=True, widget=forms.Textarea(attrs={'id': 'text-area', 'placeholder': 'Enter your name'}))
    email = forms.EmailField(label="UserEmail")
    file = forms.FileField(label="UserFile")
    # age = forms.IntegerField(label="Age")
    age = forms.CharField(widget=forms.NumberInput(), label="Age")
    weight = forms.FloatField(label="Weight")
    balance = forms.DecimalField(label="Balance")
    check = forms.BooleanField(label="Check")
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    # apointment = forms.DateTimeField(label="Apointment")
    Apointment = forms.DateTimeField(
        widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('L', 'Large'), ('M', 'Medium')]
    size = forms.ChoiceField(
        label="Size", choices=CHOICES, widget=forms.RadioSelect)
    MEAL = [('V', 'Veg'), ('N', 'Non Veg'), ('E', 'Egg')]
    pizza = forms.MultipleChoiceField(
        label="Pizza", choices=MEAL, widget=forms.CheckboxSelectMultiple)


# class StudentForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.EmailField(widget=forms.EmailInput)

#     # def clean_name(self):
#     #     Valname = self.cleaned_data['name']
#     #     if len(Valname) < 10:
#     #         raise forms.ValidationError('Name should be at least 10 letters')
#     #     return Valname

#     # def clean_email(self):
#     #     Valemail = self.cleaned_data['email']
#     #     if '.com' not in Valemail:
#     #         raise forms.ValidationError('Email must me contain .com')
#     #     return Valemail

#     def clean(self):
#         cleaned_data = super().clean()
#         valname = cleaned_data.get('name')
#         valemail = cleaned_data.get('email')

#         if valname and len(valname) < 10:
#             raise forms.ValidationError('Name should be at least 10 letters')
#         if '.com' not in valemail:
#             raise forms.ValidationError('Email must contain .com')

def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError('Name should be at least 10 letters')


class StudentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[
                           validators.MaxLengthValidator(10, message='Name should be at least 10 letters')])
    # name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message='Name should be must 10 letters')])
    email = forms.EmailField(widget=forms.EmailInput, validators=[
                             validators.EmailValidator(message='Enter a valid email')])
    age = forms.IntegerField(widget=forms.NumberInput, validators=[validators.MaxValueValidator(
        20, message='Age should be less than 20'), validators.MinValueValidator(10, message='Age should be greater than 10')])

    file = forms.FileField(validators=[validators.FileExtensionValidator(
        allowed_extensions=['pdf', 'png'], message='File should be pdf')])

    text = forms.CharField(widget=forms.TextInput, validators=[len_check])



class PasswordValidationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = cleaned_data['password']
        val_conpass = cleaned_data['confirm_password']
        val_name = cleaned_data['name']
        
        if val_pass != val_conpass:
            raise forms.ValidationError("Password doesn't match")

        if len(val_name) < 10:
            raise forms.ValidationError('Name should be at least 10 letters')