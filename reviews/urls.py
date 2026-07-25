from django.urls import path
from . import views

urlpatterns = [
    path(
        "create/<int:rental_item_id>/",
        views.create_review_view,
        name="create_review",
    ),
]