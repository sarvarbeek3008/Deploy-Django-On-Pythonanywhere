from django.urls import path

from app.views import Index, glasses, index

urlpatterns = [
    path('', index, name = 'index'),
    # path('', MaxPriceView.as_view(), name= 'index'),
    path('glasses/', glasses, name = 'glasses')
]
