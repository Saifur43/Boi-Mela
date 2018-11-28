from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(),name='home'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w\d]+)/$',views.BookDetailView.as_view(),name='details'),
]
