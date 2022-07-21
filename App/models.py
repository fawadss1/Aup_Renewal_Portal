from django.db import models


class ValidUptoDate(models.Model):
    Date = models.DateField(auto_now=False)

    def __str__(self):
        return str(self.Date)


class Semester(models.Model):
    Name = models.CharField(max_length=30)
    Fee = models.IntegerField()
    Valid_Upto_Date = models.ForeignKey(ValidUptoDate, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Department(models.Model):
    Program_Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Program_Name


class Student(models.Model):
    Name = models.CharField(max_length=30)
    Father_Name = models.CharField(max_length=30)
    Roll_No = models.IntegerField()
    Program = models.ForeignKey(Department, on_delete=models.CASCADE)
    Semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
