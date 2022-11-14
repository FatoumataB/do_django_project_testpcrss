from django.db import models

# Create your models here.

class SpaceCapsules(models.Model):
    CapsuleId = models.CharField(max_length=50)
    CapsuleSerial	= models.CharField(max_length=50)
    Status	= models.CharField(max_length = 50)		
    OriginalLaunch = models.DateTimeField()		
    Missions = models.CharField(max_length=50)		
    Landings= models.IntegerField()		
    Type	= models.CharField(max_length=50)			
    Details	= models.CharField(max_length=50)			
    ReuseCount	= models.IntegerField()	