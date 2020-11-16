from django.db import models

# Create your models here.
class Personnel(models.Model):
    idPersonnel = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    personalEmail = models.CharField(max_length=45)
    hiredate = models.DateField()
    emailMatrix = models.CharField(max_length=45)
    position = models.CharField(max_length=45)
    profession = models.CharField(max_length=45)
    note = models.CharField(max_length=45)
    status = models.BinaryField()
    code = models.IntegerField()

    class Meta():
        """
        docstring
        """
        ordering = ["hiredate"]
        db_table = "personnels"
        #models = "employee"

class Availability(models.Model):
    idAvailability = models.AutoField(primary_key=True)
    day = models.CharField(max_length=45)
    statTime = models.DateTimeField()
    endTime = models.DateTimeField()
    note = models.CharField(max_length=45)
    notavailable = models.BinaryField()
    status = models.BinaryField()
    Personnel_idPersonnel = models.IntegerField()
    
    class Meta():
        """
        docstring
        """
        ordering = ["statTime"]
        db_table = "availabilities"
        #models = "employee"

class TeacherPreference(models.Model):
    Personnels_idPersonnel = models.IntegerField()
    Cours_idCours = models.IntegerField()
    Note = models.CharField(max_length=150)
    rank = models.BinaryField()

    class Meta():
        """
        docstring
        """        
        db_table = "teacherpreferences"
        #models = "employee"
