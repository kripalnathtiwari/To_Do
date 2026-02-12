from django.shortcuts import render, redirect, get_object_or_404
from .models import List, ListItem
from .forms import ListItemForm


def list_page(request, list_id):
    mylist = get_object_or_404(List, id=list_id)

    if request.method == "POST":
        form = ListItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.list = mylist
            item.save()
            return redirect('list_page', list_id=list_id)
    else:
        form = ListItemForm()

    items = mylist.items.all()

    return render(request, "list.html", {
        "form": form,
        "items": items,
        "mylist": mylist
    })


def delete_item(request, item_id):
    item = get_object_or_404(ListItem, id=item_id)
    list_id = item.list.id
    item.delete()
    return redirect('list_page', list_id=list_id)
