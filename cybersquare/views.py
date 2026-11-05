from django.http import HttpResponse
from django.shortcuts import render
page_data={"title":"Calicut IT","description":"Where Your IT Work Experience Starts"}
project_data = {
    "projects": [
        {
            "name": "AI Chatbot",
            "description": "An intelligent chatbot using Python and AI."
        },
        {
            "name": "E-Commerce Website",
            "description": "An online shopping platform using Django."
        },
        {
            "name": "Student Management",
            "description": "A student management system using Python."
        },
        {
            "name": "Face Recognition",
            "description": "A face recognition application using OpenCV."
        },
        {
                    "name": "ERP",
                    "description": "ERP Software using python."
        }
    ]
}
def home(request):
    return render(request,"index.html",page_data)
def aboutus(request):
    return render(request,"aboutus.html",page_data)
def contactus(request):
    return render(request,"contactus.html",page_data)
def projects(request):
    context = {
        **page_data,
        **project_data
    }
    return render(request,"projects.html",context)

