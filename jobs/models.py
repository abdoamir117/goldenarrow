from django.db import models


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=128)
    location = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(help_text="", null=True, blank=True)
    requirement = models.TextField(help_text="", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    starting_date = models.DateField(null=True, blank=True)
    closing_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    # @property
    # def descriptions(self):
    #     return self.description.strip().split(",")

    # @property
    # def requirements(self):
    #     return self.requirement.strip().split(",")
