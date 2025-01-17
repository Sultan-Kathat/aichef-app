from django.db import models
from users.models import User

# Create your models here.
class Recipe(models.Model):
    MEAL_TYPE_CHOICES = (
        ("BR", "breakfast"),
        ("LC", "lunch"),
        ("DN", "dinner"),
    )

    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="name")
    recipe_date = models.DateField(blank=True, null=True, verbose_name="date")
    calorie = models.PositiveIntegerField( blank=True, null=True, verbose_name="calorie")
    protein = models.PositiveIntegerField( blank=True, null=True, verbose_name="protein")
    meal_type = models.CharField(max_length=4, choices=MEAL_TYPE_CHOICES, blank=True, null=True, verbose_name="meal type")
    user = models.ForeignKey(User, null=True, blank=True, related_name="recipes", on_delete=models.CASCADE, verbose_name="user")
    instruction = models.TextField(blank=True, null=True, verbose_name="instruction")
    #instruction will store answer from ChatGPT

    def __str__(self) -> str:
        return f"{self.id} - {self.name} {self.recipe_date} {self.meal_type} {self.user}"
    
class Equipment(models.Model):
    EQUIPMENT_TYPE_CHOICES = (
        ("ST", "Stove"),
        ("OV", "Oven"),
        ("MW", "Microwave"),
        ("ST", "Stove"),
        ("BL", "Blender"),
        ("SE", "Steamer"),
    )
   
    equipment_type = models.CharField(max_length=100, blank=True, null=True, choices=EQUIPMENT_TYPE_CHOICES, verbose_name="name")
    user = models.ForeignKey(User, null=True, blank=True, related_name="equipments", on_delete=models.CASCADE, verbose_name="user")

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"
    
