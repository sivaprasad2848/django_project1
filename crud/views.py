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

def delete_todo(request,id):
    with connection.cursor() as cursor:
                cursor.execute("delete from task_data where slno=%s",[id])
    return redirect("crud") 
def edit_todo(request, id):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM task_data WHERE slno = %s",
            [id]
        )
        task = cursor.fetchone()

    return render(request, 'edit_todo.html', {'task': task})
def update_todo(request, id):

    if request.method == 'POST':

        task = request.POST.get('task')

        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE task_data SET task_title = %s WHERE slno = %s",
                [task, id]
            )

        return redirect('crud')