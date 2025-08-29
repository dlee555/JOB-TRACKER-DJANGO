from django.contrib.auth.mixins import LoginRequiredMixin   # forces login for the view
from django.urls import reverse_lazy                        # resolves URL names at import time safely
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q                              # for OR queries in search
from .models import Application
from .forms import ApplicationForm

class ApplicationListView(LoginRequiredMixin, ListView):
    """
    Lists only the logged-in user's applications.
    Adds simple search (?q=) and status filter (?status=applied|interview|...).
    Paginated to 10 rows per page (?page=2).
    """
    model = Application
    template_name = "applications/application_list.html"    # which template to render
    context_object_name = "applications"                    # name used in template
    paginate_by = 10

    def get_queryset(self):
        # Start with only this user's rows
        qs = Application.objects.filter(user=self.request.user)

        # Optional search across company OR job_title, case-insensitive
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(Q(company__icontains=q) | Q(job_title__icontains=q))

        # Optional status filter; "all" means no filtering
        status = self.request.GET.get("status")
        if status and status != "all":
            qs = qs.filter(status=status)

        return qs

    def get_context_data(self, **kwargs):
        # Pass extra context so the template can keep form state in the UI
        ctx = super().get_context_data(**kwargs)
        ctx["q"] = self.request.GET.get("q", "")
        ctx["current_status"] = self.request.GET.get("status", "all")
        ctx["STATUS_CHOICES"] = Application.STATUS_CHOICES
        return ctx

class ApplicationCreateView(LoginRequiredMixin, CreateView):
    """
    Displays a form and creates a new Application row.
    We set form.instance.user so each new row is owned by the current user.
    """
    model = Application
    form_class = ApplicationForm
    template_name = "applications/application_form.html"
    success_url = reverse_lazy("applications:list")         # where to go on success

    def form_valid(self, form):
        form.instance.user = self.request.user              # attach owner before saving
        return super().form_valid(form)

class ApplicationUpdateView(LoginRequiredMixin, UpdateView):
    """
    Edits an existing row — but only if it belongs to the current user.
    Restricting get_queryset() prevents editing others' data by URL guessing.
    """
    model = Application
    form_class = ApplicationForm
    template_name = "applications/application_form.html"
    success_url = reverse_lazy("applications:list")

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user)

class ApplicationDeleteView(LoginRequiredMixin, DeleteView):
    """
    Confirms and deletes a row, scoped to the current user's data.
    """
    model = Application
    template_name = "applications/application_confirm_delete.html"
    success_url = reverse_lazy("applications:list")

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user)
