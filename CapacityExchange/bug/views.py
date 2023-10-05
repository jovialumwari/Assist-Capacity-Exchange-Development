from django.shortcuts import render, redirect, get_object_or_404
from .models import Bug
from .forms import BugForm  # You'll create this form later

# Create your views here.
# Landing Page 
def home(request):
    return render(request, 'bug/home.html')

# view to register a bug into the database
def register_bug(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bug_list')
    else:
        form = BugForm()
    
    return render(request, 'bug/register_bug.html', {'form': form})

# view to view the fields of a bug

def view_bug(request, bug_id):
    bug = get_object_or_404(Bug, pk=bug_id)
    return render(request, 'bug/view_bug.html', {'bug': bug})

# view to list all the bugs in the database

def bug_list(request):
    bugs = Bug.objects.all()
    return render(request, 'bug/bug_list.html', {'bugs': bugs})
   