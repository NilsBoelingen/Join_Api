from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from join_app.api.serializers import UserSerializer, TaskSerializer, SubTaskSerializer, ContactSerializer
from join_app.models import Subtask, Task, User, Contact
from django.utils import timezone

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class SubTaskViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subtask.objects.all()
    serializer_class = SubTaskSerializer

class SummaryView(APIView):
    def get(self, request):
        todo_count = Task.objects.filter(position='to-do').count()
        in_progress_count = Task.objects.filter(position='in-progress').count()
        done_count = Task.objects.filter(position='done').count()
        feedback_count = Task.objects.filter(position='feedback').count()
        urgent_count = Task.objects.filter(priority='urgent').count()
        overdue_count = Task.objects.exclude(position='done').filter(due_date__gte=timezone.now().date()).count()
        total_count = Task.objects.all().count()

        data = {
            'todo_count': todo_count,
            'in_progress_count': in_progress_count,
            'done_count': done_count,
            'feedback_count': feedback_count,
            'urgent_count': urgent_count,
            'overdue_count': overdue_count,
            'total_count': total_count
        }

        return Response(data)
    
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer