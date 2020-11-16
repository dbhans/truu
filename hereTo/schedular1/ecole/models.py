from django.db import models

# Create your models here.
class Cour(models.Model):
    idCours = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=45)
    Code = models.CharField(max_length=10)
    Unit = models.CharField(max_length=6)
    NumberHours = models.IntegerField()
    Description = models.TextField()
    status = models.BinaryField()
    """
    def __str__(self):
        return {"Nom" : self.Name,"Code" :self.Code}
    """
    class Meta():
        """
        docstring
        """
        ordering = ["NumberHours"]
        db_table = "cour"
        #model = "Classroom"

class Classroom(models.Model):
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
        #model = "Classroom"

class Program(models.Model):
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
        #model = "Classroom"

class Software(models.Model):
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
        #model = "Classroom"

class Classroom_has_Software(models.Model):
    Classroom_idClassroom = models.IntegerField()
    Softwares_idSoftware = models.IntegerField()

    class Meta():
        """
        docstring
        """ 
        db_table = "classroom_softwares"
        #model = "Classroom"

class Group(models.Model):
    idgroup = models.AutoField(primary_key=True)
    code = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    numberstudent = models.CharField(max_length=45)
    Starting = models.DateField()
    Ending = models.DateField()
    numberduration = models.IntegerField()
    numbertime = models.CharField(max_length=25)
    status = models.BinaryField()
    Created = models.DateTimeField()
    Modified = models.DateTimeField()

    class Meta:
        """
        docstring
        """
        ordering = ["Starting"]
        db_table = "groups"
        #model = "Classroom"