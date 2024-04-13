from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, "Registration successful!")
            return redirect("catalog")  # Redirect to the appropriate view
        else:
            # Registration failed, display error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(response, f"Error in {field}: {error}")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the catalog page in the catalog app
            return redirect('catalog')  
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'register/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    if request.method == 'POST':
        # Handle form submission
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.email = request.POST.get('email')
        request.user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile')
    return render(request, 'register/profile.html', {'user': request.user})