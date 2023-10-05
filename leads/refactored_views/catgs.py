from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views import generic
from django.urls import reverse_lazy
from agents.mixins import OrganisorAndLoginRequiredMixin, PermissionAndLoginRequiredMixin
from leads.models import Lead, Category
from leads.forms import CategoryModelForm, User


class CategoryListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/category_list.html"
    context_object_name = "category_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)

        context.update(
            {"unassigned_lead_count": queryset.filter(category__isnull=True).count()}
        )
        return context

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organisor:
            queryset = Category.objects.filter(organisation=user.userprofile)
        else:
            queryset = Category.objects.filter(organisation=user.agent.organisation)
        return queryset


class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/category_detail.html"
    context_object_name = "category"

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organisor:
            queryset = Category.objects.filter(organisation=user.userprofile)
        else:
            queryset = Category.objects.filter(organisation=user.agent.organisation)
        return queryset


class CategoryCreateView(PermissionAndLoginRequiredMixin, generic.CreateView):
    template_name = "leads/category_create.html"
    form_class = CategoryModelForm
    success_url = reverse_lazy("leads:category-list")

    def form_valid(self, form):
        # form.instance.organisation.set(self.request.user.userprofile)
        return super().form_valid(form)

# @receiver(post_save, sender=Category)
# def update_organisation(sender, instance, **kwargs):
#     users = User.objects.all()
#     for user in users:
#         instance.organisation.set(user.userprofile)

class CategoryDeleteView(PermissionAndLoginRequiredMixin, generic.DeleteView):
    template_name = "leads/category_delete.html"
    success_url = reverse_lazy("leads:category-list")

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organisor:
            queryset = Category.objects.filter(organisation=user.userprofile)
        else:
            queryset = Category.objects.filter(organisation=user.agent.organisation)
        return queryset


class CategoryUpdateView(PermissionAndLoginRequiredMixin, generic.UpdateView):
    template_name = "leads/category_update.html"
    form_class = CategoryModelForm
    success_url = reverse_lazy("leads:category-list")

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organisor:
            queryset = Category.objects.filter(organisation=user.userprofile)
        else:
            queryset = Category.objects.filter(organisation=user.agent.organisation)
        return queryset
