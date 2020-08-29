from django.db import models
from django.contrib.auth import get_user_model

class Project(models.Model):
    PROJECT_CATEGORIES = (  
        ("CP", "Cupcakes"),  
        ("CK", "Cake"),  
        ("FD", "Fondant"),  
        ("BC", "Buttercream"),  
        ("PS", "Pastry"),
        (None, "")
    )

    title = models.CharField(max_length=200)
    category = models.CharField(
    max_length=20,
    choices=PROJECT_CATEGORIES,
    default=None,
    null=True
    )
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete= models.CASCADE,
        related_name='owner_projects'
    )


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete= models.CASCADE,
        related_name='supporter_pledges'
    )


