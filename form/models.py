from django.db import models

CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

class ContactForm(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(choices=CHOICES, max_length=128)
    mobile = models.IntegerField(max_length=10)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.full_name
    
