from django.views import generic
from .models import Entry


class LastEntryList(generic.ListView):
    """
    Return last 10 entries that are with status 1 (published) and order from the latest one.
    """
    queryset = Entry.objects.filter(status=1).order_by('-created_at')[:10]
    template_name = 'index.html'

class EntryList(generic.ListView):
    """
    Return all entries that are with status 1 (published) and order from the latest one.
    """
    queryset = Entry.objects.filter(status=1).order_by('-created_at')
    template_name = 'all_entries.html'

class PopularEntryList(generic.ListView):
    """
    Return 5 most popular entries that are with status 1 (published) and order from the most popular one.
    """
    queryset = Entry.objects.filter(status=1).order_by('-search_count')
    template_name = 'popular_entries.html'


class EntryDetail(generic.DetailView):
    model = Entry
    template_name = 'entry_detail.html'