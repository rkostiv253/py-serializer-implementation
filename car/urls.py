from django.urls import path

from car.views import CarViewSet

car_list = CarViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})
car_detail = CarViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

urlpatterns = [
    path("car/", car_list, name="car-list"),
    path("car/<int:pk>", car_detail, name="car-detail"),
]
