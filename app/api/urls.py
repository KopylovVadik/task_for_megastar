from django.urls import path

from .views import WriterList

app_name = "api"

urlpatterns = [
    path('writer/<int:pk>/', WriterList.as_view(), name="writer_list"),
]