from django.db import models

# Create your models here.
class Cours(model.Model):
    idCours = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=45)
    Code = models.CharField(max_length=10)
    Unit = models.CharField(max_length=6)
    NumberHours = models.IntegerField()
    Description = models.TextField()
    status = models.BinaryField()

    class Meta():
        """
        docstring
        """
        ordering = ["NumberHours"]
        db_table = "cours"
        model = "Classroom"

class Classroom(model.Model):
    idClassroom = models.AutoField(primary_key=True)
    Numberplace = models.CharField(max_length=45)
    Room = models.IntegerField()
    status = models.BinaryField()
    Classroomcol = models.CharField(max_length=45)

    class Meta():
        """
        docstring
        """
        ordering = ["Room"]
        db_table = "classroom"
        model = "Classroom"

class Programs(model.Model):
    idPrograms = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=45)
    Code = models.CharField(max_length=45)
    Description = models.CharField(max_length=255)
    Requierements = models.CharField(max_length=45)
    status = models.BinaryField()
    Cours_idCours = models.IntegerField()

    class Meta():
        """
        docstring
        """
        db_table = "programs"
        model = "Classroom"

class Softwares(model.Model):
    idSoftware = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=45)
    Description = models.CharField(max_length=45)
    Type = models.CharField(max_length=45)
    Version = models.CharField(max_length=45)

    class Meta():
        """
        docstring
        """
        ordering = ["Name"]
        db_table = "softwares"
        model = "Classroom"

class Classroom_has_Softwares(model.Model):
    Classroom_idClassroom = models.IntegerField()
    Softwares_idSoftware = models.IntegerField()

    class Meta():
        """
        docstring
        """ 
        db_table = "classroom_softwares"
        model = "Classroom"

class Groups(model.Model):
    idgroup = models.AutoField(primary_key=True)
    code = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    numberstudent = models.CharField(max_length=45)
    Starting DATE NULL
    Ending DATE NULL
    numberduration = models.IntegerField()
    numbertime = models.CharField(max_length=25)
    status = models.BinaryField()
    Created = models.DateTimeField()
    Modified = models.DateTimeField()

    class Meta():
        """
        docstring
        """
        ordering = ["Starting"]
        db_table = "groups"
        model = "Classroom"