from django.urls import path
from blog import views
from blog.views import PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view()),
   path('<int:pk>/', PostDetail.as_view() ),
]

