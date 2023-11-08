from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit
from habit.serializers import HabitSerializer
from habit.permission import IsOwner, IsSafe
from habit.paginators import HabitPagination


class HabitCreateView(CreateAPIView):
    """Habit create endpoint"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()


class HabitDetailView(RetrieveAPIView):
    """Habit detail endpoint"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateView(UpdateAPIView):
    """Habit update endpoint"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class AllHabitListView(ListAPIView):
    """All public habit list endpoint"""
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsSafe]
    pagination_class = HabitPagination


class MyHabitListView(ListAPIView):
    """Private habit list endpoint"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, ]
    pagination_class = HabitPagination

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class HabitDeleteView(DestroyAPIView):
    """Habit delete endpoint"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
