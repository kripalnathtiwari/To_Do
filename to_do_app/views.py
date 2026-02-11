from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import ListItem
from .forms import ListItemForm
# Create your views here.
def home(request):
    return render("add_task.html")
def add_task(request):
    return redirect(request, "add_task.hmtl")



def list_page(request):

    if request.method == "POST":
        form = ListItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_page')

    else:
        form = ListItemForm()

    items = ListItem.objects.all()

    return render(request, "list.html", {
        "form": form,
        "items": items
    })
