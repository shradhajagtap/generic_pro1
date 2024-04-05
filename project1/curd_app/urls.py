from django.urls import path
from .views import StudentCreate, StudentList, StudentDetail, StudentUpdate, StudentDelete

urlpatterns = [
    path('', StudentCreate.as_view()),
    path("list/", StudentList.as_view()),
    path("detail/<pk>/", StudentDetail.as_view()),
    path("update/<pk>/", StudentUpdate.as_view()),
    path("delete/<pk>/", StudentDelete.as_view()),
]
