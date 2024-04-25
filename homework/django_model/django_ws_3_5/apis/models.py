from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

class APIInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    api_url = models.URLField(validators=[MinLengthValidator(15), MaxLengthValidator(60)])
    documentation_url = models.URLField()
    auth_required = models.BooleanField()
    additional_info = models.JSONField(blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
