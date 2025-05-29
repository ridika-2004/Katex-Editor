# editor/views.py
from django.shortcuts import render, redirect
from .models import MathExpression

def editor_view(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        if content.strip():  # Only save if there's actual content
            MathExpression.objects.create(content=content)
        return redirect('editor')  # Redirect to avoid duplicate submissions
    
    expressions = MathExpression.objects.all().order_by('-created_at')
    return render(request, 'editor/editor.html', {'expressions': expressions})