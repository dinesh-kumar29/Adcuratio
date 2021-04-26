from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    age =  models.IntegerField()
    gender = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNo = models.IntegerField()

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Employee.objects.all()




class User(models.Model):
    first_name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)


    @staticmethod
    def get_email_id(email):
        try:
            return User.objects.get(email=email)
        except:
            return False

    def register(self):
        self.save()
    def userExits(self):
        if User.objects.filter(email=self.email):
            return True
        return False

    def __str__(self):
        return self.name
