from django.shortcuts import redirect, render
from lists.models import Item, List
from django.http import HttpResponse

# Create your views here.
# home_page = None


# def home_page(request):
#     return HttpResponse("<html><title>To-Do lists</title></html>")

# def home_page(request):
#     if request.method == "POST":
#         return HttpResponse("You submitted: " + request.POST["item_text"])

#     return render(request, "home.html")

def home_page(request):
    # if request.method == "POST":
    #     Item.objects.create(text=request.POST["item_text"])

    # item = Item()
    # item.text = request.POST["item_text"]
    # item.save()
    # return redirect(request, "home.html")
    # items = Item.objects.all()
    # return render(request, "home.html", {"items": items})
    return render(request, "home.html")


def view_list(request, list_id):
    our_list = List.objects.get(id=list_id)
    # items = Item.objects.filter(list=our_list)
    return render(request, "list.html", {"list": our_list})


def new_list(request):
    nulist = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=nulist)
    return redirect(f"/lists/{nulist.id}/")

    # return render(
    #     request,
    #     "home.html",
    #     {"new_item_text": request.POST.get("item_text", "")},
    # )


def add_item(request, list_id):
    our_list = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST["item_text"], list=our_list)
    return redirect(f"/lists/{our_list.id}/")
