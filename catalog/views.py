from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Company, Project, User, Manager, ContactPhones, ContactEmail, Connection
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    context = {}
    context['num_companys'] = Company.objects.all().count()
    context['num_projects'] = Project.objects.all().count()
    context['num_users'] = User.objects.all().count()
    return render(request, 'index.html', context=context)


class CompanyListView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'company_list.html'
    paginate_by = 3

    def get_ordering(self):
        ordering = self.request.GET.get('sort', 'name_company')
        return ordering if ordering in {'name_company', '-name_company', 'created_at',
                                        '-created_at'} else \
            'name_company'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        context['current_order'] = self.get_ordering()
        return context

class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = Company
    template_name = 'company_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['managerphone'] = ContactPhones.objects.select_related('name_company').filter(
            name_company=self.kwargs['pk']).all()
        context['manageremail'] = ContactEmail.objects.select_related('name_company').filter(
            name_company=self.kwargs['pk'])
        context['projects'] = Project.objects.select_related('company').filter(
            company=self.kwargs['pk'])
        return context


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'project_list.html'
    paginate_by = 10

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'project_detail.html'

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user_detail.html'

class ConnectionListView(LoginRequiredMixin, ListView):
    model = Connection
    template_name = 'connection_list.html'

class ConnectionDetailView(LoginRequiredMixin, DetailView):
    model = Connection
    template_name = 'connection_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ConnectionDetailView, self).get_context_data(**kwargs)
        context['company'] = Company.objects.prefetch_related('project_set').get(pk=self.kwargs[
            'pk'])
        return context

class CompanyUpdate(LoginRequiredMixin, UpdateView):
    model = Company
    fields = '__all__'
    template_name = 'company_update.html'

class CompanyCreate(LoginRequiredMixin, CreateView):
    model = Company
    fields = "__all__"
    template_name = 'company_create.html'

class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    fields = '__all__'
    template_name = 'project_create.html'

class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    fields = '__all__'
    template_name = 'project_update.html'

class ConnectionCreate(LoginRequiredMixin, CreateView):
    model = Connection
    fields = '__all__'
    template_name = 'connection_create.html'

class ConnectionUpdate(LoginRequiredMixin, UpdateView):
    model = Connection
    fields = '__all__'
    template_name = 'connection_update.html'

class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'photo', 'email']
    template_name = 'user_update.html'