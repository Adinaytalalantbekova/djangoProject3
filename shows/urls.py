from django.urls import path
from . import views

urlpatterns = [

    path("shows/", views.ShowsListView.as_view(), name="shows_all"),
    path("shows/<int:id>/", views.ShowsDetailView.as_view(), name="shows_detail"),
    path("shows/<int:id>/update/", views.ShowsUpdateView.as_view(), name="show_update"),
    path("shows/<int:id>/delete/", views.ShowsDeleteView.as_view(), name="show_update"),
    path("add-show/", views.ShowsCreateView.as_view(), name="add_show"),

    path('shows/', views.shows_all, name='shows_all'),
    path('shows/<int:id>/', views.shows_detail, name='shows_detail'),
    path('shows/<int:id>/delete/', views.show_delete, name='show_update'),
    path('add-show/', views.add_show, name='add_show'),

]

