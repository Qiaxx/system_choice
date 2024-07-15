from django.shortcuts import render
from django.views.generic import TemplateView


class ContactsView(TemplateView):
    template_name = "system/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        print(f"name: {name}, phone: {phone}, message: {message}")

        return render(request, self.template_name)


def base(request):
    return render(request, "system/base.html")
