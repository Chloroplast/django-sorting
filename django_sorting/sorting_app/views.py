from django import forms
from django.shortcuts import render
from timeit import default_timer

from sorting_app.models import SortRun
from sorting_app.sorting_algorithms.SortingAlgorithmFactory import SortingAlgortihmFactory


class SortForm(forms.ModelForm):
    class Meta:
        model = SortRun
        fields = ['algorithm', 'data']


def index(request):
    sorted_data = ""

    if request.method == "POST":
        form = SortForm(request.POST)
        if form.is_valid():
            new_sort = form.save(commit=False)

            if new_sort.algorithm != "Bubble":
                new_sort.algorithm = "Python Default"

            sorting_algorithm = SortingAlgortihmFactory.build(new_sort.algorithm)
            data_to_sort = new_sort.data

            start_time = default_timer()
            new_sort.data = sort(data_to_sort, sorting_algorithm)
            end_time = default_timer()
            new_sort.elapsed_time = end_time - start_time

            sorted_data = new_sort.data
            new_sort.save()

    return render(request, "index.html",
                  {"num_sorting_runs": SortRun.objects.count(),
                   "form": SortForm(),
                   "sorted_data": sorted_data})


def sort(data, algorithm):
    data_list = data_string_to_int_list(data)

    algorithm.sort(data_list)

    data_string = data_int_list_to_string(data_list)
    return data_string


def data_string_to_int_list(data):
    data_as_list = data.split(",")
    data_as_list = [int(i) for i in data_as_list]
    return data_as_list


def data_int_list_to_string(data_list):
    data_list = [str(i) for i in data_list]
    separator = ","
    data_string = separator.join(data_list)
    return data_string


def history(request):
    return render(request, "history.html",
                  {"past_runs": SortRun.objects.all()})
