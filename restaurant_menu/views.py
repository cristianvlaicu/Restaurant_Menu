from django.shortcuts import render  # Imports the render function from django.shortcuts
from django.views import generic  # Imports generic views from django.views
from .models import Item, MEAL_TYPE  # Imports the Item model and the MEAL_TYPE constant from models


class MenuList(generic.ListView):  # Defines a class MenuList that inherits from the generic ListView
    queryset = Item.objects.order_by("-date_created")  # Defines a queryset to order Item objects by creation date in descending order
    template_name = "index.html"  # Specifies the template to use, in this case "index.html"

    def get_context_data(self, **kwargs):  # Defines a method to get context data
        context = super().get_context_data(**kwargs)  # Calls the parent class's get_context_data method and stores the context
        context['meals'] = MEAL_TYPE  # Adds the MEAL_TYPE constant to the context under the key 'meals'
        return context  # Returns the updated context


class MenuItemDetail(generic.DetailView):  # Defines a class MenuItemDetail that inherits from the generic DetailView
    model = Item  # Specifies that the model to use is Item
    template_name = "menu_item_detail.html"  # Specifies the template to use, in this case "menu_item_detail.html"

