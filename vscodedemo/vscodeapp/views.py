from django.shortcuts import render
from .models import Task

def tasklist():
    tasks=Task.object.all().order_by("created_at")

    if request.method
    
