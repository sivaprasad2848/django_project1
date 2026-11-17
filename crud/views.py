from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def index(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT slno, task_title FROM task_data ORDER BY slno DESC")
        tasks = cursor.fetchall()
    return render(request,"todo.html",{'tasks': tasks})
def insert_todo(request):
    if request.method == "POST":
           task = request.POST.get('task')
           #print(task)
           #pasted
           with connection.cursor() as cursor:
                cursor.execute("INSERT INTO task_data (task_title) VALUES (%s)",[task])
           #pasted
    return redirect("crud")  