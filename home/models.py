from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=30)
    desc = models.TextField()


    def __str__(self):#for displaying the object name
        return self.name +" - "+self.email
       
