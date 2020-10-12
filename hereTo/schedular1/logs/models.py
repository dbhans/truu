from django.db import models

# Create your models here.
class  Logs(models.Model):
    creation = models.DateTimeField()
    modified = models.DateTimeField()
    createdBy = models.IntegerField()
    modifiedBy = models.IntegerField()
    tableName = models.CharField(max_length=15)
    modifiedField = models.CharField(max_length=15)
    lastValue = models.TextField(max_length=255)

    class Meta():
      
        pass

class AdminComments(models.Model):
    comment = models.TextField()
    