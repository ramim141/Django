from django import forms
from .models import PracticeModel 

class PracticeForm(forms.Form):
    # CharField()
    name = forms.CharField()
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)
    # comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    # agree = forms.BooleanField(required=False)
    agree = forms.BooleanField()
    # date  = forms.DateField()
    date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    DATE_CHOICES = ['1980', '1981', '1982']
    BirthYear = forms.ChoiceField(widget=forms.widgets.Select, choices=[
                                  (x, x) for x in DATE_CHOICES])
    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)

    
    duration = forms.DurationField( ) 
    file  = forms.FileField()
    
    
    
    
    
    # Model forms here
    
class PracticeModelForm(forms.ModelForm):
    class Meta:
        model = PracticeModel 
        fields = '__all__'