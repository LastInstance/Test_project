from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Group
from django.utils import timezone


def index(request):
    return render(request, 'users_list/index.html')

def users(request):
    users = User.objects.all()
    return render(request, 'users_list/users.html', {'users': users})

def groups(request):
    groups = Group.objects.all()
    return render(request, 'users_list/groups.html', {'groups': groups})

def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        group_id = request.POST['group']
        group = Group.objects.get(pk=group_id)
        user = User(username=username, created=timezone.now(), group=group)
        user.save()
        return redirect('/users')

    groups = Group.objects.all()
    return render(request, 'users_list/add_user.html', {'groups': groups})

def edit_user(request, user_id):
    user = User.objects.get(pk=user_id)
    groups = Group.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username', '')
        group_id = request.POST.get('group', '')

        if username and group_id:
            group = Group.objects.get(pk=group_id)  # Retrieve the Group instance
            user.username = username
            user.group = group  # Assign the Group instance
            user.save()
            return redirect('/users')  # Redirect to the list of users after editing

    return render(request, 'users_list/edit_user.html', {'user': user, 'groups': groups})

def del_user(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == "POST":
        user.delete()
        return redirect("/users")

    return render(request, 'users_list/del_user.html', {'user': user})

def add_group(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        group = Group(name=name, description=description)
        group.save()
        return redirect('/groups')

    return render(request, 'users_list/add_group.html')

def edit_group(request, group_id):
    group = Group.objects.get(pk=group_id)

    if request.method == 'POST':
        group.name = request.POST['name']
        group.description = request.POST['description']
        group.save()
        return redirect('/groups')

    return render(request, 'users_list/edit_group.html', {'group': group})


def delete_group(request, group_id):

    group = Group.objects.get(pk=group_id)
    users_in_group = User.objects.filter(group=group)

    if request.method == 'POST':
        if users_in_group.exists():
            return redirect('/groups')
        else:
            group.delete()
            return redirect('/groups')

    return render(request, 'users_list/delete_group.html', {'users_in_group': users_in_group, 'group': group})





