from django.db import models

class adminLogin(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

#foremployeecreate
class Employee(models.Model):
    employeeid=models.AutoField(primary_key=True)
    password=models.CharField(max_length=30 ,default=False)
    name=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    cno=models.IntegerField()
    email=models.EmailField(max_length=30)


class recuirtment(models.Model):
    oppcode=models.IntegerField(primary_key=True)
    qualification=models.CharField(max_length=30)
    startregistration=models.DateField()
    age=models.IntegerField()
    lastregistration=models.DateField()
    deptid=models.CharField(max_length=10)
    position=models.IntegerField()
    description=models.CharField(max_length=100)
    responsibilities=models.CharField(max_length=250)
    cno=models.IntegerField()


class applicant(models.Model):
    name=models.CharField(max_length=40,default=False)
    dob=models.DateField(default=False)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=20,default=False)
    gender=models.CharField(max_length=10,default=False)
    mobile=models.IntegerField(default=False)
    address=models.CharField(max_length=60,default=False)

class applicationform(models.Model):
    name=models.CharField(max_length=40)
    dob=models.DateField()
    email=models.EmailField(max_length=20)
    gender=models.CharField(max_length=10)
    mob=models.IntegerField()
    address=models.CharField(max_length=60)
    qualification=models.CharField(max_length=20)
    post=models.CharField(max_length=10)
    percentage=models.DecimalField(max_digits=10,decimal_places=2)
    resume=models.FileField(upload_to='resume')

    def __str__(self):
        return str(self.id)

class Interviewschedule(models.Model):
    idno=models.IntegerField()
    empid=models.IntegerField(default=False)
    date=models.DateField()

class Finalinterview(models.Model):
    inter_id =models.IntegerField()
    interviewer = models.IntegerField()
    schedule = models.CharField(max_length=30)
    appid = models.IntegerField()
    res = models.CharField(max_length=20)
    # def __str__(self):
    #     return str(self.id)
