from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'LearningSheet/index.html', {
        'error_message': "You didn't select a choice.",
    })
    