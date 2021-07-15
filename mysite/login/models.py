from django.db import models


class Sign_in(models.Model):
    username = models.CharField(max_length=120, blank=False, null=False)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    password = models.CharField(max_length=150, blank=False, null=False)

    @property
    def __str__(self):
        return self.username
