from django.db import models

# Create your models here.


class TestM(models.Model):
    TestName = models.CharField(max_length=255)
    MaxMarks = models.IntegerField()
    TimeDuration = models.IntegerField()
    PosMarks = models.IntegerField()
    NegMarks = models.IntegerField()
    inputText = models.TextField()
    mimeType = models.CharField(max_length=50)
    InputTextFile = models.FileField(upload_to='Test.TestM/inputText/TestName/mimeType', blank=True, null=True)

    def __unicode__(self):
        return self.TestName
