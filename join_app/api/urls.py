from django.urls import path, include
from rest_framework import routers
from join_app.api.views import SubTaskViewSet, TaskViewSet, UserViewSet, SummaryView

router = routers.SimpleRouter()
router.register(r'user', UserViewSet)
router.register(r'task', TaskViewSet)
router.register(r'subtask', SubTaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('summary/', SummaryView.as_view(), name='summary'),
]
