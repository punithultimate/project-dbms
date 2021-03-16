from . import views
from django.urls import path

app_name = 'waste'
urlpatterns = [
    path('',views.IndexClassView.as_view(),name='index'),
    path('<int:pk>/',views.WasteDetail.as_view(),name='detail'),
    path('issue/',views.issue,name='issue'),
    path('add',views.create_issue,name='create_issue'),
    path('update/<int:id>/', views.update_issue,name='update_issue'),
    path('delete/<int:id>/', views.delete_issue,name='delete_issue'),
]