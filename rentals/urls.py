from django.urls import path

from . import views

urlpatterns = [

    path(
        "create/<int:product_id>/",
        views.create_rental,
        name="create_rental",
    ),

]