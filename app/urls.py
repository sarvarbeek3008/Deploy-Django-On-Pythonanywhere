from django.urls import path

from app.views import Index, glasses, MaxPriceView

urlpatterns = [
    # path('', Index.as_view(), name = 'index'),
    path('', MaxPriceView.as_view(), name= 'index'),
    path('glasses/', glasses, name = 'glasses')
]
