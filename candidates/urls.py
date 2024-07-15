from django.urls import path

from candidates.apps import CandidatesConfig
from candidates.views import (
    CandidateListView,
    CandidateDetailsView,
    CandidateUpdateView,
    CandidateDeleteView, CandidateCreateView,
)

app_name = CandidatesConfig.name

urlpatterns = [
    path("", CandidateListView.as_view(), name="candidate_list"),
    path(
        "candidate-details/<int:pk>",
        CandidateDetailsView.as_view(),
        name="candidate_details",
    ),
    path(
        "candidate-update/<int:pk>",
        CandidateUpdateView.as_view(),
        name="candidate_update",
    ),
    path(
        "candidate-delete/<int:pk>",
        CandidateDeleteView.as_view(),
        name="candidate_delete",
    ),
    path(
        "candidate-create/",
        CandidateCreateView.as_view(),
        name="candidate_create",
    ),
]
