from django.urls import path

from . import views

app_name="polls" #Important to be called on template html file ex: <a href="{% url polls.<path_name> id(optional) %}></a>"

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:question_id>/',views.details,name='details'),
    path('<int:question_id>/result/',views.result,name='result'),
]