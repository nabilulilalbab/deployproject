from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Feedback
from .forms import FeedbackForm

@login_required
def feedback_list(request):
    feedbacks = Feedback.objects.all().order_by('-id')
    return render(request, 'feedback/feedback_list.html', context={'feedbacks': feedbacks})


@login_required
def add_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('feedback:list')
        else:
            print(form.errors)  # Tambahkan ini saat debugging
    else:
        form = FeedbackForm()
    return render(request, 'feedback/add_feedback.html', {'form': form})

