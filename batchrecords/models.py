from django.db import models

class BatchJob(models.Model):
    # In order to gracefully handle omissions, I will make the fields optional:
    batch_number = models.IntegerField(null=True, blank=True),
    submitted_at = models.CharField(max_length=32, null=True, blank=True),
    nodes_used = models.IntegerField(null=True, blank=True)
