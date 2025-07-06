from django.urls import path
from .views import ListingListCreate,  ListingRetrieveUpdateDestroy # ✅ this line

urlpatterns = [
    path("listings/", ListingListCreate.as_view(), name="listing-list"),
    path("listings/<uuid:pk>/", ListingRetrieveUpdateDestroy.as_view(), name="listing-detail"),
]