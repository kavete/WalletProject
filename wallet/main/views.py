from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def blog_details(request):
    return render(request, "blog_details.html")


def blog(request):
    return render(request, "blog.html")


def contact(request):
    return render(request, "contact.html")


def faq(request):
    return render(request, "faq.html")


def how_it_works(request):
    return render(request, "how_it_works.html")


def legal(request):
    return render(request, "legal.html")


def privacy_policy(request):
    return render(request, "privacy_policy.html")


def service_details(request):
    return render(request, "service_details.html")


def services(request):
    return render(request, "services.html")


def terms(request):
    return render(request, "terms.html")

