
from django.urls import path
from . import views
from employee.views import EmployeeViews, EmployeeDetailViews    

urlpatterns = [
    path('students/', views.studentsViews),
    path('student/<int:pk>/', views.studentDetailViews),
    path('employees/',  EmployeeViews.as_view()),
    path('employee/<int:pk>/', EmployeeDetailViews.as_view()),      

]
