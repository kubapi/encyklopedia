from django.views import generic
from .models import Entry
from .forms import EntryCreateForm

class LastEntryList(generic.ListView):
    """
    Return last 10 entries or that are with status 1 (published) and order from the latest one or return queried one
    """
    template_name = 'index.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            entries_list = Entry.objects.filter(word__icontains=query, status=1)
            for entry in entries_list:
                entry.search_count += 1
                entry.save()
        else:
            entries_list = Entry.objects.filter(status=1).order_by('-created_at')[:10]

        return entries_list

class EntryList(generic.ListView):
    """
    Return all entries that are with status 1 (published) and order from the latest one.
    """
    queryset = Entry.objects.filter(status=1).order_by('-created_at')
    paginate_by = 5
    template_name = 'all_entries.html'

class PopularEntryList(generic.ListView):
    """
    Return 5 most popular entries that are with status 1 (published) and order from the most popular one.
    """
    queryset = Entry.objects.filter(status=1).order_by('-search_count')[:5]
    template_name = 'popular_entries.html'

class EntryDetail(generic.DetailView):
    model = Entry
    template_name = 'entry_detail.html'

class EntryCreate(generic.CreateView):
    template_name = 'entry_create.html'
    form_class = EntryCreateForm