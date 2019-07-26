from django.shortcuts import render, HttpResponse, redirect, reverse

# Create your views here.
def index(request):
    kwgs = {
        "project_name":"超级项目",
        "project_info1": ["超级项目1","这是一个xxxx的项目"],
        "project_info2": {"name":"超级项目2","desc":"这是一个项目2"},
        "good_students": [{"name":"jack","hobby":"basketball"},
                          {"name":"Ding","hobby":"tv"},
                          {"name":"li","hobby":"reading"},
                          {"name":"hetao","hobby":"study"},
                          ]
    }
    return render(request, "django_templates/index.html",kwgs)