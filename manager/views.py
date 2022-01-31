from django.views import generic
from .models import Entry


class EntryList(generic.ListView):
    """
    Return all entries that are with status 1 (published) and order from the latest one.
    """
    queryset = Entry.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'


class EntryDetail(generic.DetailView):
    model = Entry
    template_name = 'entry_detail.html'