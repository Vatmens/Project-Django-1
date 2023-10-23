from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = Articles.objects.order_by('-data')
    return render(request, "news/news_home.html", {'news': news})
# Create your views here.

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/news_delete.html'
    success_url = '/news/'


class NewsDetailViev(DetailView):
    model = Articles
    template_name = 'news/news-detail.html'
    context_object_name = 'article'


def create(request):
    form = ArticlesForm()
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Text not correct'

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)
