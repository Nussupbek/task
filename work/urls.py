from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.work_home, name='work_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.WorkDetailView.as_view(), name='work-detail'),
    path('<int:pk>/update', views.WorkUpdateView.as_view(), name='work-update'),
    path('<int:pk>/delete', views.WorkDeleteView.as_view(), name='work-delete')
]
