from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    edit_id = request.GET.get('edit')

    if request.method == "POST":

        # ADD TASK
        if "add_task" in request.POST:
            Task.objects.create(title=request.POST.get("title"))
            return redirect('task_list')

        # UPDATE TASK TITLE
        if "update_task" in request.POST and request.POST.get("task_id"):
            task = get_object_or_404(Task, id=request.POST.get("task_id"))
            task.title = request.POST.get("title")
            task.save()
            return redirect('task_list')

        # TOGGLE DONE
        if "toggle_done" in request.POST and request.POST.get("task_id"):
            task = get_object_or_404(Task, id=request.POST.get("task_id"))
            task.completed = 'completed' in request.POST
            task.save()
            return redirect('task_list')

        # ✅ FALLBACK (CRITICAL)
        return redirect('task_list')

    # GET request
    filter_type = request.GET.get('filter')

    if filter_type == 'completed':
        tasks = Task.objects.filter(completed=True)
    elif filter_type == 'pending':
        tasks = Task.objects.filter(completed=False)
    else:
        tasks = Task.objects.all()
    
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    if total_tasks > 0:
        progress_percent = int((completed_tasks / total_tasks) * 100)
    else:
        progress_percent = 0
    return render(request, 'todo/task_list.html', {
        'tasks': tasks,
        'edit_id': edit_id,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'filter_type': filter_type, 
        'progress_percent': progress_percent,  # 👈 IMPORTANT

    })

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

