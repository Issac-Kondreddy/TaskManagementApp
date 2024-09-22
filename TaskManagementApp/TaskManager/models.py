from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db import models

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    task_status_choices = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    task_status = models.CharField(max_length=100, choices=task_status_choices, default='Pending')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.task_name

    # Add model-level validation
    def clean(self):
        # Validate task_name
        if len(self.task_name) < 5:
            raise ValidationError({
                'task_name': _('Task name should be at least 5 characters long.')
            })
        
        # Validate task_description
        if len(self.task_description) < 10:
            raise ValidationError({
                'task_description': _('Task description should be at least 10 characters long.')
            })

        # Validate task_status
        valid_status = ['Pending', 'In Progress', 'Completed']
        if self.task_status not in valid_status:
            raise ValidationError({
                'task_status': _('Task status must be one of: %(valid_status)s.'),
                'params': {'valid_status': ', '.join(valid_status)}  # Corrected syntax
            })

    # Override save method to call clean() before saving
    def save(self, *args, **kwargs):
        self.clean()  # Ensure the clean method is called before saving
        super(Tasks, self).save(*args, **kwargs)
