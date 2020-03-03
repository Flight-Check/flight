from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from flight_detail.models import Flightinfo


class Index(TemplateView):
    template_name = 'index.html'


class Search(View):
    template_name = 'search.html'

    def post(self, request, *args, **kwargs):
        flight_number = self.request.POST.get('flight')
        data = Flightinfo.objects.filter(flightnumbers=flight_number)
        context = {"data": data}
        return render(request, self.template_name, context)
