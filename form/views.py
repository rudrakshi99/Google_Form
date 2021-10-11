from django.shortcuts import render
from django.http import HttpResponse
from .forms import Contact
from .models import ContactForm
from .tasks import send_email

def contact(request):
    
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            mobile = form.cleaned_data['mobile']
            address = form.cleaned_data['address'] 
            info = ContactForm(full_name=full_name, email=email, gender=gender, 
                    mobile=mobile, address=address)
            info.save()        
            send_email.delay(email)
            return HttpResponse('Thank you for your information.')
    form = Contact()
    return render(request, 'contact.html', {'form': form})