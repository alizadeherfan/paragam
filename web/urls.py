from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^submit/markets/$', views.submit_markets, name ='submit_markets'),
    url(r'^submit/income/$', views.submit_income, name ='submit_income'),
]
