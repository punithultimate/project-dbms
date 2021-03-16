from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Issue
from .forms import IssueForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


def index(request):
    issue_list=Issue.objects.all()
    context={
        'issue_list':issue_list,
    }
    return render(request,'waste/index.html',context)


class IndexClassView(ListView):
    model = Issue;
    template_name = 'waste/index.html'
    context_object_name = 'issue_list'


def issue(request):
    return HttpResponse('<h1>  this is heading</h1>')


def detail(request,issue_id):
    issue=Issue.objects.get(pk=issue_id)
    context = {
        'issue':issue,
    }
    return render(request,'waste/detail.html',context)


class WasteDetail(DetailView):
    model = Issue;
    template_name = 'waste/detail.html'


def create_issue(request):
    form = IssueForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('waste:index')
    return render(request,'waste/issue-form.html',{'form':form})


def update_issue(request,id):
    issue = Issue.objects.get(id=id)
    form = IssueForm(request.POST or None, instance=issue)
    if form.is_valid():
        form.save()
        return redirect('waste:index')
    return render(request,'waste/issue-form.html',{'form':form,'issue':issue})


@login_required
def delete_issue(request,id):
    issue = Issue.objects.get(id=id)
    if request.method == 'POST':
        issue.delete()
        return redirect('waste:index')
    return render(request, 'waste/issue-delete.html', { 'issue': issue})