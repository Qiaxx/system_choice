from django.contrib import admin

from candidates.models import Candidate


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name")
    list_filter = ("full_name",)
    search_fields = ("full_name", "date_of_birth")
