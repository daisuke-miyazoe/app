from rest_framework.viewsets import ModelViewSet
from my_api.models import Task
from my_api.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_fields = {
        'complete_flag': ['exact'],
    }