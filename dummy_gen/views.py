from django.shortcuts import render, redirect

# Create your views here.

from dummy_gen.forms import SchemeForm
from dummy_gen.models import Scheme

import datetime

from django.template import loader

from django.views.generic import UpdateView, DeleteView

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from dummy_gen.tasks import datagenerate
from django.views.generic import *
from django.shortcuts import *


def load(request):
    task = go_to_sleep.delay(1)
    return render(request, 'load.html', {'task_id': task.task_id})


def scheme_create(request):
    user = request.user
    user = user.id
    success_url = '/list'

    if request.method == 'POST':
        form = SchemeForm(request.POST, initial={'author': user})

        if form.is_valid():
            form.save()
            return redirect('/list')

    return render(request, 'scheme_form.html', {'form': SchemeForm(initial={'author': user}), })


def scheme_list(request):
    user = request.user

    queryset = Scheme.objects.filter(author=user)
    print(queryset)

    context = {"object_list": queryset}
    return render(request, "scheme_list.html", context)


class scheme_edit(UpdateView):
    template_name = "scheme_edit.html"
    form_class = SchemeForm
    success_url = '/list'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Scheme, id=id_)


class scheme_delete(DeleteView):
    template_name = "scheme_delete.html"
    success_url = '/list'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Scheme, id=id_)

    def get_success_url(self):
        return "/list"


def do(request, id=None):
    # Get scheme
    scheme = Scheme.objects.get(id=id)
    scheme_id = int(scheme.id)
    print(scheme)
    print(scheme.id)
    print(int(scheme.id))

    # COLUMNS
    # Get columns
    columns = []

    columns.append(scheme.c1)
    columns.append(scheme.c2)
    columns.append(scheme.c3)
    columns.append(scheme.c4)
    columns.append(scheme.c5)
    columns.append(scheme.c6)
    columns.append(scheme.c7)
    columns.append(scheme.c8)
    columns.append(scheme.c9)

    # Replace IDs with names
    col_names = {'1': 'Choose...',
                 '2': 'name',
                 '3': 'job',
                 '4': 'company',
                 '5': 'date',
                 '6': 'phone',
                 '7': 'address',
                 '8': 'city',
                 '9': 'country',
                 '10': 'email', }

    def replace(list, dictionary):
        for idx, val in enumerate(list):
            list[idx] = dictionary[list[idx]]
        return list
    replace(columns, col_names)
    while 'Choose...' in columns:
        columns.remove('Choose...')

    print ('Columns: ')
    print(columns)

    # NAMES
    # Get names
    names = []

    names.append(scheme.n1)
    names.append(scheme.n2)
    names.append(scheme.n3)
    names.append(scheme.n4)
    names.append(scheme.n5)
    names.append(scheme.n6)
    names.append(scheme.n7)
    names.append(scheme.n8)
    names.append(scheme.n9)

    while '' in names:
        names.remove('')

    while 'None' in names:
        names.remove('None')

    print('Names of columns: ')
    print(names)

    # ORDER
    # Get order
    order = []

    order.append(scheme.o1)
    order.append(scheme.o2)
    order.append(scheme.o3)
    order.append(scheme.o4)
    order.append(scheme.o5)
    order.append(scheme.o6)
    order.append(scheme.o7)
    order.append(scheme.o8)
    order.append(scheme.o9)

    while 0 in order:
        order.remove(0)

    print('Order: ')
    print(order)

    if order:
        columns = [x for _, x in sorted(zip(order, columns))]
        names = [x for _, x in sorted(zip(order, names))]

    print('Columns in order: ')
    print(columns)
    print(names)

    rows = scheme.rows
    print('Number of rows:')
    print(rows)

    filename = str(scheme.author) + '_' + str(scheme.name) + '_' + str(datetime.datetime.today().strftime('%Y-%m-%d_%H-%M-%S')) + '.csv'

    task = datagenerate.delay(rows, columns, names, filename, scheme_id)
    print(filename)

    return render(request, 'load.html', {'task_id': task.task_id})
