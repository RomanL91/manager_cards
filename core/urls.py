from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(("manager_card.urls", "manager_card"), namespace="manager_card"))
]
