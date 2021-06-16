from django.contrib import admin
from django.urls import path
from .utils import *

urlpatterns = [
    path('branches/', get_branches ),
    path('branch/<str:branch>', branch),
    path('clone/', clone_repo),
    path('commit/', add_and_commit_changes),

]
