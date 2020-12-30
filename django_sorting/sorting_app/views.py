from django import forms
from django.shortcuts import render
from timeit import  default_timer

from sorting_app.models import SortRun


class SortForm(forms.ModelForm):
    class Meta:
        model = SortRun
        fields = ['algorithm', 'data']


def index(request):
    if request.method == "POST":
        form = SortForm(request.POST)
        if form.is_valid():
            new_sort = form.save(commit=False)

            start_time = default_timer()
            sort(new_sort.data)
            end_time = default_timer()

            new_sort.elapsed_time = end_time - start_time
            new_sort.save()

    return render(request, "index.html",
                  {"num_sorting_runs": SortRun.objects.count(),
                   "form": SortForm()})


def sort(data):
    return list.sort(data.split(","))
