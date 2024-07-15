from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from candidates.forms import CandidateForm
from candidates.models import Candidate


class CandidateListView(ListView):
    model = Candidate


class CandidateDetailsView(DetailView):
    model = Candidate


class CandidateCreateView(CreateView):
    model = Candidate
    form_class = CandidateForm
    success_url = reverse_lazy("candidates:candidate_list")

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class CandidateUpdateView(UpdateView):
    model = Candidate
    form_class = CandidateForm
    success_url = reverse_lazy("candidates:candidate_details")

    def get_success_url(self):
        return reverse("candidates:candidate_details", args=[self.kwargs.get("pk")])


class CandidateDeleteView(DeleteView):
    model = Candidate
    success_url = reverse_lazy("candidates:candidate_list")
