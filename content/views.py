from django.shortcuts import render
from .forms import PostingForm
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import PrePosting, Posting

# Create your views here.
def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def preposting(request):
    if request.method == 'POST':
        form = PostingForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/payment-form/')

    else:
        form = PostingForm()
    return render(request, 'update.html', {'form': form})

def payment_form(request):
    prepost = PrePosting.objects.last()
    position_title = prepost.position_title.title()
    client_name = prepost.client_name.title()
    date = prepost.date
    position_city = prepost.position_city.title()
    states = prepost.states.all
    position_description = prepost.position_description.capitalize()
    position_link = prepost.position_link
    legal_list = prepost.legal_field.all
    return render(request, "money.html", {"position_title": position_title, "client_name": client_name,"date": date,"position_city": position_city,"position_description": position_description,"position_link": position_link, "legal_list": legal_list, "states": states}
)

def checkout(request):

    prepost = PrePosting.objects.last()

    new_posting = Posting(
    position_title=prepost.position_title.title(),
    client_name=prepost.client_name.title(),
    date=prepost.date,
    position_city=prepost.position_city.title(),
    position_description=prepost.position_description.capitalize(),
    posted_by=prepost.posted_by,
    position_link=prepost.position_link,
    accept_terms=prepost.accept_terms,
    )
    new_posting.save()
    postpost = Posting.objects.last()
    c = prepost.legal_field.all()
    postpost.legal_field.set(c)
    d = prepost.states.all()
    postpost.states.set(d)
    return render(request, 'cool.html')



def LegalInfo(request):
    return render(request, 'legal.html')