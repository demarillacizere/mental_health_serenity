from datetime import datetime
from django.urls import reverse_lazy
from django.views import View
from rest_framework.reverse import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *
from .serializers import *
from .forms import UserRegistrationForm, UserLoginForm

User = get_user_model()


class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class ProfessionalDashboardView(DetailView):
    model = Professional
    template_name = "professional_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        professional = get_object_or_404(Professional, user=self.request.user)
        appointments = Appointment.objects.filter(professional=professional)
        context['appointments'] = appointments
        context['new_clients'] = appointments.count()
        context['appointments_count'] = appointments.count()
        return context


class UserDashboardView(DetailView):
    model = User
    template_name = "user-dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        appointments = Appointment.objects.filter(user=user)
        context['appointments'] = appointments
        context['appointments_count'] = appointments.count
        return context


class UserRegistrationView(View):
    template_name = "registration/register.html"
    form_class = UserRegistrationForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            user = User.objects.create_user(
                password=password1, email=email, first_name=first_name, last_name=last_name)
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'registration/register.html', {'form': form})


class UserLoginView(View):
    template_name = 'registration/login.html'
    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                if user.is_professional:
                    professional = get_object_or_404(Professional, user=user)
                    return redirect(reverse('professional-dashboard', kwargs={'pk': professional.id}))
                elif user.is_staff:
                    return redirect('/admin/')
                else:
                    return redirect(reverse('dashboard', kwargs={'pk': user.id}))

        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})


class ProfessionalsListView(ListView):
    model = Professional
    template_name = 'professionals_list.html'


class ProfessionalDetailView(DetailView):
    model = Professional
    template_name = 'professional_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ResourcesListView(ListView):
    model = Resource
    paginate_by = 50
    template_name = 'resource_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddResourceForm()
        return context


class ResourceCreateView(CreateView):
    model = Resource
    form_class = AddResourceForm
    success_url = reverse_lazy('resources')

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return render(self.request, 'resource_list.html', {'form': form})


class AppointmentView(View):
    def post(self, request, *args, **kwargs):
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        duration = int(request.POST.get('duration'))
        purpose = request.POST.get('purpose')
        status = request.POST.get('status')
        # print(request.POST.get('professional'))
        professional = get_object_or_404(
            Professional, id=request.POST.get('professional'))

        # Calculate end time
        start_datetime = datetime.combine(datetime.strptime(
            date, '%Y-%m-%d').date(), datetime.strptime(start_time, '%H:%M').time())
        end_datetime = start_datetime + timedelta(minutes=duration)
        end_time = end_datetime.time()
        user = self.request.user
        appointment = Appointment.objects.create(
            date=date,
            start_time=start_time,
            end_time=end_time,
            purpose=purpose,
            status=status,
            professional=professional,
            user=user,
            duration=duration
        )

        # Redirect or render success message
        return redirect(reverse('dashboard', kwargs={'pk': user.id}))


class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()

        for post in posts:
            comments = Comment.objects.filter(post=post)
            post.comment_count = comments.count()
            # Use set() method to set related objects
            post.comments.set(comments[:3])
            # post.remaining_comments.set(comments[3:])
            print(post.comments)

        return render(request, 'chat_corner.html', {'posts': posts})


def create_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            # Process the form data
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            post = Post(title=title, content=content, user=request.user)
            post.save()
            # Save the post or perform any other action
            return redirect(reverse('community'))
    else:
        form = NewPostForm()
    return render(request, 'create_post.html', {'form': form})

def approve_appointment(request, appointment_id, *args, **kwargs):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    professional = get_object_or_404(Professional, user=request.user)

    # Perform approval logic (e.g., update status)
    appointment.status = 'Approved'
    appointment.save()

    # Redirect back to the professional dashboard or any desired page
    return redirect(reverse('professional-dashboard', kwargs={'pk': professional.id}))