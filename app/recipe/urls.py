"""
URL mappings for the recipe API.
"""
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)


# app_name is looking by test
app_name = 'recipe'

urlpatterns = [
    path('recipe/', include(router.urls)),
]
