from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Card, Resource, Session

# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# Add the following import
from django.http import HttpResponse

from .forms import SessionForm

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


@login_required
def cards_index(request):
    cards = Card.objects.filter(user=request.user)
    return render(request, 'cards/index.html', { 'cards': cards })


@login_required
def cards_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    resources_card_doesnt_have = Resource.objects.exclude(id__in = card.resources.all().values_list('id'))
    # total_time = 0
    # sessions = Feeding.objects
    # for x in sessions:
    #     # total_time+= x
    #     print(x)
    session_form = SessionForm()
    return render(request, 'cards/detail.html', {
        'card': card, 'session_form': session_form,
        'resources': resources_card_doesnt_have, 
        # 'time' : total_time
    })
@login_required
def add_session(request, card_id):
    form = SessionForm(request.POST)
    if form.is_valid():
        new_session = form.save(commit=False)
        new_session .card_id = card_id
        new_session .save()
    return redirect('detail', card_id=card_id)
@login_required
def assoc_resource(request, card_id, resource_id):
    Card.objects.get(id=card_id).resources.add(resource_id)
    return redirect('detail', card_id=card_id)
@login_required
def assoc_resource_delete(request, card_id, resource_id):
    Card.objects.get(id=card_id).resources.remove(resource_id)
    return redirect('detail', card_id=card_id)
# signup
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    # turtle
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class CardCreate(LoginRequiredMixin, CreateView):
    model = Card
    fields = ['goal', 'topic', 'description', 'hours']
    success_url = '/cards/'
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  
    # Let the CreateView do its job as usual
        return super().form_valid(form)


class CardUpdate(LoginRequiredMixin, UpdateView):
    model = Card
    fields = ['topic', 'description', 'hours']

class CardDelete(LoginRequiredMixin, DeleteView):
    model = Card
    success_url = '/cards/'

class ResourceList(LoginRequiredMixin, ListView):
    model = Resource
    template_name = 'resources/index.html'

class ResourceDetail(LoginRequiredMixin, DetailView):
    model = Resource
    template_name = 'resources/detail.html'

class ResourceCreate(LoginRequiredMixin, CreateView):
    model = Resource
    fields = ['link', 'description']


class ResourceUpdate(LoginRequiredMixin, UpdateView):
    model = Resource
    fields = ['link', 'description']


class ResourceDelete(LoginRequiredMixin, DeleteView):
    model = Resource
    success_url = '/resources/'
