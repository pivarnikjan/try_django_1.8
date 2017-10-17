from django.core.mail import send_mail
from django.shortcuts import render

from trydjango18.settings import EMAIL_HOST_USER
from .forms import ContactForm, SignUpForm


def home(request):
    title = "Welcome"
    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get('full_name')

        if not full_name:
            instance.full_name = "Justin Bieber"
        instance.save()
        context = {
            "title": "Thank you"
        }

    return render(request, "base.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key, value in form.cleaned_data.items():
        #     print(key, value)
        form_full_name = form.cleaned_data.get("full_name")
        form_message = form.cleaned_data.get("message")
        form_email = form.cleaned_data.get("mail")

        subject = "Site contact form"
        from_email = EMAIL_HOST_USER
        to_email = [from_email]

        contact_message = "%s: %s via %s" % (form_full_name, form_message, form_email)
        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)

    context = {
        "form": form,
    }
    return render(request, "forms.html", context)
