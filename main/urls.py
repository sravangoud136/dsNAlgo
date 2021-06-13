from django.urls import path
from main import views
urlpatterns = [
    path('',views.index,name="home"),
    path('problems',views.showproblems,name="showproblems"),
    path('problemswithtag/<str:tag>',views.problemswithtag,name="problemswithtag"),
    path('viewproblem/<int:pk>',views.viewproblem,name="viewproblem")
]
