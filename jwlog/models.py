from django.db import models

class Log(models.Model):

    log_path = models.CharField(max_length=100)
    create_time = models.DateTimeField(null=True)
    filename = models.CharField(max_length=40)
    project_own = models.CharField(max_length=40)
    is_remote = models.CharField(max_length=40)

    def __unicode__(self):
        return self.log_path