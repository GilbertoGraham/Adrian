from django.urls import path

from . import views
from .pollViews.QuestionViews import QuestionDetailView, QuestionResponseView

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('timestamp', views.timestamp, name='timestamp'),
    path('<int:question_id>/', QuestionDetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', QuestionResponseView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]