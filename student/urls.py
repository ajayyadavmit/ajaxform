from django.urls import path
from .views import home , save_data, newForm, home_value, home_value2

urlpatterns = [
    path('home/',home),
    path('save/',save_data, name='save'),
    path('form/',newForm),
    path('home/<int:value>/',home_value, name='homevalue'),
    path('home/<int:value>/<int:value2>',home_value2, name='homevalue'),

]
