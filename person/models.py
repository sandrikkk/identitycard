from django.db import models

class sex(models.Model):
    class Meta:
        verbose_name = "sexs"
        verbose_name_plural = "Sex" 
    sex = models.CharField(max_length=50)
    def __str__(self):
        return self.sex
class Department(models.Model):
    department = models.CharField(max_length=150, null = True)

    def __str__(self):
        return self.department

class Person(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to = "images/")
    cardnum = models.CharField(max_length = 9, unique = True)
    city = models.CharField(max_length=50)
    sex = models.ForeignKey(sex, on_delete=models.SET_NULL, null = True)
    personalid = models.CharField(max_length=11, unique=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    dateofbirth = models.DateField()
    dateofexpiry = models.DateField()

    def __str__(self):
        return f"{self.name} {self.last_name}"

