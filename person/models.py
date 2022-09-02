from django.db import models

class sex(models.Model):
    class Meta:
        verbose_name = "sexs"
        verbose_name_plural = "Sex" 
    sex = models.CharField(max_length=50)
    def __str__(self):
        return self.sex

class ParentDepartment(models.Model):
    parentdepartment = models.CharField(max_length=150)

    def __str__(self):
        return self.parentdepartment

class ChildDepartment(models.Model):
    parentdepartment = models.ForeignKey(ParentDepartment, on_delete=models.CASCADE)
    department = models.CharField(max_length=150, null = True)

    def __str__(self):
        return f"{self.parentdepartment}/{self.department}"

class Characteristics(models.Model):
    class Meta:
        verbose_name = "characteristicss"
        verbose_name_plural = "characteristics" 
    characteristics = models.CharField(max_length=150)

    def __str__(self):
        return self.characteristics


class Person(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to = "images/")
    cardnum = models.CharField(max_length = 9, unique = True)
    city = models.CharField(max_length=50)
    sex = models.ForeignKey(sex, on_delete=models.SET_NULL, null = True)
    personalid = models.CharField(max_length=11, unique=True)
    department = models.ForeignKey(ChildDepartment, on_delete=models.DO_NOTHING, null = True)
    characteristics = models.ManyToManyField(Characteristics)
    dateofbirth = models.DateField()
    dateofexpiry = models.DateField()

    def __str__(self):
        return f"{self.name} {self.last_name} - {self.department} - დან"
class Monitoring(models.Model):
    movida = models.DateTimeField()
    wavida = models.DateTimeField()
    comment = models.TextField(max_length=255)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return f"{self.person}"