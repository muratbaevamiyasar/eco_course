from django.db import models

class Lecture(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    pdf = models.FileField(upload_to="lectures/")

    def __str__(self):
        return self.title


class Practice(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    pdf = models.FileField(upload_to="practice/")

    def __str__(self):
        return self.title


class Resource(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    pdf = models.FileField(upload_to="resources/")

    def __str__(self):
        return self.title