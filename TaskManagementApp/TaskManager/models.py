from django.db import models

# Create your models here.
class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    task_status_choices = [
        ('Pending','Pending'),
        ('In Progress','In Progress'),
        ('Completed','Completed'),
    ]
    task_status = models.CharField(max_length=100, choices = task_status_choices, default = 'Pending')
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now =True)
    deleted_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.task_name
