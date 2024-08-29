from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import UserForm

# List all users.
def index(request):
  user_list = User.objects.all()
  return render(request, "user_list.html", {"users": user_list})


# Add a user...
def add_user(request):
  if (request.method == 'POST'):
    form = UserForm(request.POST)
    if (form.is_valid()):
      form.save()
      messages.success(request, "'" + request.POST['names'] + "' added to list of users")
      return redirect('users')
  else:
    form = UserForm()
  return render(request, "add_user.html", {"form": form})


# Update user details...
def update_user(request, user_id):
  user = User.objects.get(id=user_id)
  if (request.method == 'POST'):
    form = UserForm(request.POST, instance=user)
    form.save()
    messages.success(request, "User details updated successfully")
    return redirect('users')
  else:
    form = UserForm(instance=user)
    
  return render(request, "update_user.html", {"form": form, "user_id":user.id})


# Remove a user
def delete_user(request, user_id):
  user = User.objects.get(id=user_id)
  if (user.id):
    user.delete()
    messages.success(request, "'" + user.names + "' removed successfully")
  
  return redirect("users")
