from rest_framework import viewsets, status
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
        todo_count = Task.objects.filter(position='Todo').count()
        in_progress_count = Task.objects.filter(position='InProgress').count()
        done_count = Task.objects.filter(position='Done').count()
        feedback_count = Task.objects.filter(position='AwaitFeedback').count()
        urgent_count = Task.objects.filter(urgency='urgent').count()
        overdue_count = Task.objects.exclude(position='done').filter(date__gte=timezone.now().date()).count()
        total_count = Task.objects.all().count()
        next_task = Task.objects.filter(date__gte=timezone.now().date()).exclude(position='done').exclude(urgency='low').exclude(urgency='medium').exclude(urgency='').order_by('date').first()
        next_deadline = next_task.date if next_task else 'None'

        data = {
            'todo_count': todo_count,
            'in_progress_count': in_progress_count,
            'done_count': done_count,
            'feedback_count': feedback_count,
            'urgent_count': urgent_count,
            'overdue_count': overdue_count,
            'total_count': total_count,
            'next_deadline': next_deadline
        }

        return Response(data)
    
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        tasks = Task.objects.all()
        for task in tasks:
            if instance in task.assignedTo.all():
                task.assignedTo.remove(instance)
                task.save()
                
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)