from django.db import models


class Tags(models.Model):
    TagID = models.AutoField(primary_key=True)
    TagName = models.CharField(max_length=32)
    Description = models.CharField(max_length=256)
    TagType = models.CharField(max_length=256,default='FeatureTag')
    CreatedTime = models.DateTimeField()

    class Meta:
        db_table = 'tbltag'


class Releases(models.Model):
    ReleaseID = models.AutoField(primary_key=True)
    ProductID = models.IntegerField()
    ReleaseTag = models.CharField(max_length=32)
    ReleaseName = models.CharField(max_length=32)
    Description = models.CharField(max_length=512)

    class Meta:
        db_table = 'tblrelease'
