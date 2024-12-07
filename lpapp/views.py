from django.http import JsonResponse
from django.shortcuts import render,redirect
from .forms import AppointmentForm,WebinarForm  
from .models import Team
from .forms import TeamForm,ReviewForm
from .models import Team, Review
from django.shortcuts import get_object_or_404


def home(request):
    if request.method == 'POST':
        # Check if the form submission is for the AppointmentForm
        if 'firstname' in request.POST:
            appointment_form = AppointmentForm(request.POST)
            if appointment_form.is_valid():
                appointment_form.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': appointment_form.errors.as_json()})
        
        # Check if the form submission is for the EnrollmentForm
        elif 'name' in request.POST:
            enrollment_form = WebinarForm(request.POST)
            if enrollment_form.is_valid():
                enrollment_form.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': enrollment_form.errors.as_json()})
    
    # Handle GET requests
    else:
        appointment_form = AppointmentForm()
        enrollment_form = WebinarForm()
        team_members = Team.objects.all()  # Fetch all team members
    
    return render(request, 'home.html', {
        'form': appointment_form,
        'enrollment_form': enrollment_form,
        'team_members': team_members,  # Pass the team members to the template
    })




def service(request):
    return render(request,"services.html")

def blog(request):
    return render(request,"blog.html")


def teamupdate(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lpapp:home')  # Redirect to a page listing all team members
    else:
        form = TeamForm()
    return render(request, 'teamupdate.html', {'form': form})




def profile(request, pk):
    team_member = get_object_or_404(Team, pk=pk)
    reviews = Review.objects.filter(team_member=team_member).order_by('-created_at')

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.team_member = team_member
            review.save()

            # Check if the request is AJAX
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({"message": "Review submitted successfully!"}, status=200)

            return redirect('lpapp:profile', pk=pk)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({"error": "Invalid form submission."}, status=400)

    else:
        form = ReviewForm()

    return render(request, 'profile.html', {
        'team_member': team_member,
        'reviews': reviews,
        'form': form,
    })