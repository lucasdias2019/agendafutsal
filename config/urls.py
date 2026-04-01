from django.contrib import admin
from django.urls import path
from app.views import IndexView, EquipesView, AgendamentosView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('equipes/', EquipesView.as_view(), name='equipes'),
    path('agendamentos/', AgendamentosView.as_view(), name='agendamentos'),
]