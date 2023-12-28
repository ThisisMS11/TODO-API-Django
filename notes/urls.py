from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "notes"

router = DefaultRouter()
router.register("",views.NoteViewSet)

urlpatterns=[
    path("",include(router.urls)),
]