from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=60, unique=True, db_index=True)
    
    def __unicode__(self):
        return "<project: %s>" %(self.name)


class MailTemplate(models.Model):
    name = models.CharField(verbose_name="Template Name",max_length=80, unique=True, db_index=True)
    body = models.TextField(verbose_name="Template Body")
    project = models.ForeignKey(Project)
    
    def __unicode__(self):
        return "<template: %s>" %(self.name)
    
