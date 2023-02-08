from django.shortcuts import render
from django.views import View
from django.db.models import Avg, Max, Min
from app.models import Glases


class Index(View):
    template_name = 'index.html'
# class Glasses(View):
#     template_name = 'glasses.html'

def index(request):
    model = Glases.objects.order_by('-id')
    model2 =   Glases.objects.all().aggregate(Max('price'))
    context = {
        'glassess':model,
        'prices':model2
    }
    return render(request, 'index.html', context)
def glasses(request):
    return render(request, 'glasses.html')

#
# class MaxPriceView(View):
#     def get(self, request):
#         # max_price = Glases.objects.all().aggregate(Max('price'))['price__max']
#         model = Glases.objects.order_by('-id')
#         return render(request, 'index.html', {'max_price': max_price}, {'glassess':model})