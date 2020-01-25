from django.shortcuts import render
from accounts.forms import ContactUsForm 
from django.core.mail import EmailMessage
# Create your views here.
def about_me(request):
    """
    A View that renders the about me page
    """
    return render(request, "about.html")
    
def faq_page(request):
    return render(request, "faq.html")

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            from_email = form.cleaned_data.get('from_email')
            message = form.cleaned_data.get('message')
            name = form.cleaned_data.get('name')
            
            message_format = "{0} has sent you a message\n\n{1}".format(name, message)
            msg = EmailMessage(
            subject, 
            message_format, 
            to=['contact@geertdeveloper.online'], 
            from_email=from_email
            )
            msg.send()
            
            return render(request, "contact_send.html")
    
    else:
        form = ContactUsForm
        
    return render(request, "contact.html", {'form': form})