from django.db import models  # Imports the models module from Django
from django.contrib.auth.models import User  # Imports the User model from Django's authentication system

# Defines a constant tuple for meal types
MEAL_TYPE = (
    ("starters", "Starters"),  # Option for starters
    ("salads", "Salads"),  # Option for salads
    ("main_dishes", "Main Dishes"),  # Option for main dishes
    ("desserts", "Desserts")  # Option for desserts
)

# Defines a constant tuple for item status
STATUS = (
    (0, "Unavailable"),  # Option for unavailable status
    (1, "Available")  # Option for available status
)

# Defines a class Item which inherits from models.Model
class Item(models.Model):  # Defines a class Item which inherits from models.Model
    meal = models.CharField(max_length=1000, unique=True)  # Defines a CharField for meal with max length 1000 and unique constraint
    description = models.CharField(max_length=2000)  # Defines a CharField for description with max length 2000
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Defines a DecimalField for price with 10 digits and 2 decimal places
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)  # Defines a CharField for meal type with max length 200 and choices from MEAL_TYPE
    author = models.ForeignKey(User, on_delete=models.PROTECT)  # Defines a ForeignKey relation to the User model with PROTECT on delete
    status = models.IntegerField(choices=STATUS, default=1)  # Defines an IntegerField for status with choices from STATUS and default value 1
    date_created = models.DateTimeField(auto_now_add=True)  # Defines a DateTimeField for date created with auto_now_add set to True
    date_updated = models.DateTimeField(auto_now=True)  # Defines a DateTimeField for date updated with auto_now set to True

    def __str__(self):  # Defines the string representation of the model
        return self.meal  # Returns the meal name
