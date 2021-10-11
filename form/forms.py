from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Submit, Layout, Div
from .models import ContactForm
    


class NameWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        super().__init__([
           forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'First Name'}),
           forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'})
        ], attrs)
    
        
    def decompress(self, value):
        if value:
            return value.split(' ')
        return ['', '']
  
  
        
class NameField(forms.MultiValueField):
    
    widget = NameWidget
    
    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(max_length=100),
            forms.CharField(max_length=100),
        )
        self.label = 'Full Name'
        self.help_text = 'First and last name'
        
        super(NameField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        return ' '.join(data_list)



class Contact(forms.ModelForm):
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'] = NameField()
        
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        
        self.helper.layout = Layout(
            Div(
                Div(
                    Field('full_name'),
                    css_class='col'
                ),
                css_class='row'
            ) ,
            
            'email',
            'gender',
            'mobile',
            'address',
            Submit('submit','Submit', css_class='btn-submit')
        )
        
    class Meta:
        model = ContactForm
        fields = ['full_name', 'email', 'gender',  'mobile', 'address']
        labels = {'email' : 'Email', 'mobile':'Mobile', 'address' : 'Address'}
        help_text = {'email' : 'Enter your email', 'mobile' : 'Enter your phone number', 
                        'address' : 'Enter your address'}
        
        widgets = {
            'full_name' : NameWidget, 
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your email'}),
            'mobile' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter your phone number'}),
            'gender' : forms.RadioSelect(choices=(('M','Male'),('F','Female'))),
            'address' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter your address'})
        }