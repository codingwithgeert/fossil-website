from django.shortcuts import render
# Create your views here.
def about_me(request):
    """
    A View that renders the about me page
    """
    return render(request, "about.html")
