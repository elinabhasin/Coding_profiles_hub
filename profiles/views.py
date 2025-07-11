from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib import messages 

def home(request):
    """
    Renders the home page of the website.
    """
    return render(request, 'profiles/home.html')

def user_list(request):
    """
    Fetches all UserProfile objects from the database and displays them.
    The profiles are ordered by creation date (newest first).
    """
    users = UserProfile.objects.all()
    context = {
        'users': users
    }
    return render(request, 'profiles/user_list.html', context)

def submit_profile(request):
    """
    Handles the submission of a new user profile.
    If the request method is POST, it attempts to save the new profile.
    If the request method is GET, it displays an empty form.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        github = request.POST.get('github')
        leetcode = request.POST.get('leetcode')
        codeforces = request.POST.get('codeforces')

      
        if not name or not email:
            messages.error(request, "Name and Email are required fields.")
            return render(request, 'profiles/submit_profile.html', {
                'name': name, 'email': email, 'github': github,
                'leetcode': leetcode, 'codeforces': codeforces
            })

        try:
         
            UserProfile.objects.create(
                name=name,
                email=email,
                github=github,
                leetcode=leetcode,
                codeforces=codeforces
            )
            messages.success(request, "Profile submitted successfully!")
            return redirect('user_list') 
        except Exception as e:
            messages.error(request, f"Error submitting profile: {e}")
            return render(request, 'profiles/submit_profile.html', {
                'name': name, 'email': email, 'github': github,
                'leetcode': leetcode, 'codeforces': codeforces
            })
    else:
        return render(request, 'profiles/submit_profile.html')

