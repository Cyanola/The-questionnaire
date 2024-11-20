from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    path("", views.index, name="index"),
     path('<int:question_id>/', views.detail, name='detail'),  # Страница опроса
    path('<int:question_id>/results/', views.results, name='results'),  # Результаты опроса
    path('<int:question_id>/vote/', views.vote, name='vote'),  # Голосование
   path('summary/', views.summary, name='summary'),
]