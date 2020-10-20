# https://docs.djangoproject.com/en/3.1/ref/models/fields/
class Cours(model.Model):
  idCours = models.AutoField(primary_key=True)
  name = models.CharField(max_length=45)
  code = models.CharField(max_length=10)
  Unit = models.CharField(max_length=6)
  NumberHours = models.IntegerField()
  Description = models.TextField()
  status = models.BinaryField()

class Classroom(model.Model):
  idClassroom = models.AutoField(primary_key=True)
  Numberplace = models.CharField(max_length=45)
  Room = models.IntegerField()
  status = models.BinaryField()
  Classroomcol = models.CharField(max_length=45)

class Programs(model.Model):
  idPrograms = models.AutoField(primary_key=True)
  Name = models.CharField(max_length=45)
  Code = models.CharField(max_length=45)
  Description = models.CharField(max_length=255)
  Requierements = models.CharField(max_length=45)
  status = models.BinaryField()
  Cours_idCours = models.IntegerField()

class Personnels(model.Model):
  idPersonnel = models.AutoField(primary_key=True)
  firstName = models.CharField(max_length=45)
  lastName = models.CharField(max_length=45)
  personalEmail = models.CharField(max_length=45)
  emailMatrix = models.CharField(max_length=45)
  position = models.CharField(max_length=45)
  profession = models.CharField(max_length=45)
  note = models.CharField(max_length=45)
  status = models.BinaryField()
  code = models.IntegerField()

class Availability(model.Model):
  idAvailability = models.AutoField(primary_key=True)
  day = models.CharField(max_length=45)
  statTime = models.DateTimeField()
  endTime = models.DateTimeField()
  note = models.CharField(max_length=45)
  notavailable = models.BinaryField()
  status = models.BinaryField()
  Personnel_idPersonnel = models.IntegerField()

class group(model.Model):
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

class Time(model.Model):
  idTime = models.AutoField(primary_key=True)
  startTime = models.DateTimeField()
  endTime = models.DateTimeField()

class Semesters(model.Model):
  idSemesters = models.AutoField(primary_key=True)
  semester = models.CharField(max_length=15)
  startTime = models.DateTimeField()
  endTime = models.DateTimeField()

class Schedule(model.Model):
  Classroom_idClassroom = models.IntegerField()
  group_idgroup = models.IntegerField()
  Personnel_idPersonnel = models.IntegerField()
  Cours_idCours = models.IntegerField()
  Time_idTime = models.IntegerField()
  Semesters_idSemesters = models.IntegerField()
  idSchedule = models.AutoField(primary_key=True)

class Logs(model.Model):
  idlog = models.AutoField(primary_key=True)
  creation = models.DateTimeField()
  modified = models.DateTimeField()
  createdBy = models.IntegerField()
  modifiedBy = models.IntegerField()
  tableName = models.CharField(max_length=45)
  modifiedField = models.CharField(max_length=45)
  lastValue = models.CharField(max_length=45)

class TeacherPreferences(model.Model):
  Personnels_idPersonnel = models.IntegerField()
  Cours_idCours = models.IntegerField()
  Note = models.CharField(max_length=150)
  rank = models.BinaryField()

class AdminComments(model.Model):
  idAdminComments = models.AutoField(primary_key=True)
  Comment = models.CharField(max_length=255)

class Softwares(model.Model):
  idSoftware = models.AutoField(primary_key=True)
  Name = models.CharField(max_length=45)
  Description = models.CharField(max_length=45)
  Type = models.CharField(max_length=45)
  Version = models.CharField(max_length=45)

class Classroom_has_Softwares(model.Model):
  Classroom_idClassroom = models.IntegerField()
  Softwares_idSoftware = models.IntegerField()


"""
from PRIMARY KEY
delete 9 

`


CREATE TABLE IF NOT EXISTS\s+(\w+)\s\(
class $1(model.Model):

(\w+)\s+INT\s+NOT\s+NULL\s+AUTO_INCREMENT,
$1 = models.AutoField(primary_key=True)

(\w+)\s+VARCHAR\((\d+)\)\s+NULL,
$1 = models.CharField(max_length=$2)



(\w+)\s+INT\s+(NULL|NOT NULL),
$1 = models.IntegerField()

(\w+)\s+DATETIME\s+NULL,
$1 = models.DateTimeField()

(\w+)\s+BIT\(.*
$1 = models.BinaryField()

(\w+)\s+MEDIUMTEXT\s+.*
$1 = models.TextField()
"""