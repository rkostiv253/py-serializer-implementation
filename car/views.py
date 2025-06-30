from rest_framework import viewsets, mixins

from car.models import Car
from car.serializers import CarSerializer


class CarViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
