from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Card, Toy

# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# Add the following import
from django.http import HttpResponse

from .forms import FeedingForm

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
    toys_card_doesnt_have = Toy.objects.exclude(id__in = card.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'cards/detail.html', {
        'card': card, 'feeding_form': feeding_form,
        'toys': toys_card_doesnt_have
    })
@login_required
def add_feeding(request, card_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.card_id = card_id
        new_feeding.save()
    return redirect('detail', card_id=card_id)
@login_required
def assoc_toy(request, card_id, toy_id):
    Card.objects.get(id=card_id).toys.add(toy_id)
    return redirect('detail', card_id=card_id)
@login_required
def assoc_toy_delete(request, card_id, toy_id):
    Card.objects.get(id=card_id).toys.remove(toy_id)
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
    fields = ['name', 'topic', 'description', 'hours']
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

class ToyList(LoginRequiredMixin, ListView):
    model = Toy
    template_name = 'toys/index.html'

class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy
    template_name = 'toys/detail.html'

class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = ['link', 'description']


class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ['link', 'description']


class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = '/toys/'
