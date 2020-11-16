from django.db import models

# Create your models here.

class Time(models.Model):
    idTime = models.AutoField(primary_key=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()

    class Meta():
        """
        docstring
        """
        ordering = ["startTime","endTime"]
        db_table = "Times"
        #models = "scheduler"

class Semester(models.Model):
    idSemesters = models.AutoField(primary_key=True)
    semester = models.CharField(max_length=15)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()

    class Meta():
        """
        docstring
        """
        ordering = ["startTime"]
        db_table = "semesters"
        #models = "scheduler"

class Schedule(models.Model):
    Classroom_idClassroom = models.IntegerField()
    group_idgroup = models.IntegerField()
    Personnel_idPersonnel = models.IntegerField()
    Cours_idCours = models.IntegerField()
    Time_idTime = models.IntegerField()
    Semesters_idSemesters = models.IntegerField()
    idSchedule = models.AutoField(primary_key=True)

    class Meta():
        """
        docstring
        """
        ordering = ["Semesters_idSemesters"]
        db_table = "schedule"
        #models = "scheduler"

class Log(models.Model):
    idlog = models.AutoField(primary_key=True)
    creation = models.DateTimeField()
    modified = models.DateTimeField()
    createdBy = models.IntegerField()
    modifiedBy = models.IntegerField()
    tableName = models.CharField(max_length=45)
    modifiedField = models.CharField(max_length=45)
    lastValue = models.CharField(max_length=45)

    class Meta():
        """
        docstring
        """
        ordering = ["creation"]
        db_table = "logs"
        #models = "scheduler"


class AdminComment(models.Model):
    idAdminComments = models.AutoField(primary_key=True)
    Comment = models.CharField(max_length=255)
    creation = models.DateTimeField()
    class Meta():
        """
        docstring
        """
        ordering = ["creation"]
        db_table = "admincomments"
        #models = "scheduler"