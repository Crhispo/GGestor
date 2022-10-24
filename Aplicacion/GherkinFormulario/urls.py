from django.urls import path
from Aplicacion.GherkinFormulario.views import CasoPruebaListView

urlpatterns = [
    path('', CasoPruebaListView.as_view(), name='Index'),
]