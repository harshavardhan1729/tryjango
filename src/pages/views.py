from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def home_view(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    #return HttpResponse("<h1> hello world</h1>")
    return render(request,"home.html",{})
def contact_view(request,*args,**kwargs):
   # return HttpResponse("<h1> hello world contact page</h1>")
    return render(request,"contact.html",{})
def about_view(request,*args,**kwargs):
    my_context={
        "my_text":"this sis contxt in my context",
        "my_number":1729,
      #  "this_is_true":True,
        "my_list":[12,354,452],

    }
    
    return render(request,"about.html",my_context) 