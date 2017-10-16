from django.shortcuts import render
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

    return render(request, "home.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        for key, value in form.cleaned_data.items():
            print(key, value)

    context = {
        "form": form,
    }
    return render(request, "forms.html", context)
