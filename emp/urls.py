from django.urls import path
from emp.views import add_emp, emp_home

urlpatterns = [
    path('home/', emp_home),
     path('add-emp/', add_emp),

]