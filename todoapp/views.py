from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from todoapp.models import Todo
# Create your views here.

def index(request):
    todo_items=Todo.objects.all().order_by("-added_date")
    return render(request,'index.html',
    {
        "todo_items":todo_items
    }
    )
@csrf_exempt
def add_todo(request):

   # print(request.POST)
    
    current_date=timezone.now()
    content=request.POST["content"]  
    #print(content)
    
    create_obj=Todo.objects.create(added_date=current_date, text=content)
    #print(create_obj)
    #print(create_obj.id)
    length_of_todo=Todo.objects.all().count()
    #print(length_of_todo)
    return HttpResponseRedirect("/")
@csrf_exempt
def delete_todo(request,Todo_id):
    Todo.objects.get(id=Todo_id).delete()
    #print(Todo_id)
    return HttpResponseRedirect("/")




