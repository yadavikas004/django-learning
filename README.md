# django-learning
Learning Python Framework Django

# Learning #
What is Django?
1.Django is python web framework
2.Django is backend server side web framework.
3.Django makes easier to build web pages using python.
   Take cares of difficult stuff so that we can concentrate on building web apps.
4.Provides many built in features.

# MVT #

Django follows MVT design patterns:

Model - data we want to present, usually data from a database
View - A request handler that returns the relevant template and content - based on the request from the user.
Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data.

# 

Set up the Environment
Download and install python
Check you pip is working
Install Django
	pip install Django
	django-admin --version
	django-admin startproject <projectname>
	python manage.py startapp login
	python manage.py runserver
	python manage.py migrate
	python manage.py makemigrations
	python manage.py startapp emp
	python manage.py createsuperuser

# 

Lets Understand
.Project structure
.URLs					URLs Define
.Views					functions & classes
.Templates				HTML Templates
.Models-CRUD OPERATIONS

# Let build employee management

Add Employee
View Employee
Delete Employee
Update Employee

#

from website.models import Student
student=Student(name="Durgesh",college="ABC",age=22,is_active=True)
student.name
student.college
student.age
student.save()
x=Student.objects.get(id=1)
x.name
all=Student.objects.all()
for i in all:
	print(i.name)
