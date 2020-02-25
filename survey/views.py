from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template, render_to_string
from fpdf import FPDF, HTMLMixin
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import PostForm

from weasyprint import HTML
from weasyprint.fonts import FontConfiguration

from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
)
from .models import Post


def index(request):
    posts = Post.objects.order_by('date_posted').filter(is_complete=True)

    context = {
        'posts': posts
    }

    return render(request, 'survey/surveys.html', context)

def post_form(request):
	form = PostForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'survey/post_form.html', context)    

# def post_form(request):
# 	tasks = Task.objects.all()

# 	form = PostForm()

# 	if request.method =='POST':
# 		form = TaskForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('/')


# 	context = {'post':post, 'form':form}
# 	return render(request, 'tasks/list.html', context)

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post
    }

    return render(request, 'survey/survey2.html', context)

# def survey_new2(request):

#     return render(request, 'survey/survey-new2.html')

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy('dashboard')
    fields = ['coordinator',            
                  'date_of_contact',
                  'student_surname',
                  'hostfamily',
                  'student_eng_name',
                  'st_1',
                  'st_1a',
                  'st_2',
                  'st_3',
                  'st_4',
                  'st_4a',
                  'st_4b',
                  'st_5',
                  'st_5a',
                  'st_6',
                  'st_6a',
                  'st_6b',
                  'st_7',
                  'st_7a',
                  'st_7b',
                  'st_coordinator_comments',
                  # Host Family Progress Report
                  'hf_hostfamily_name',
                  'hf_1',
                  'hf_1a',
                  'hf_2',
                  'hf_3',
                  'hf_3a',
                  'hf_3b',
                  'hf_4',
                  'hf_4a',
                  'hf_4b',
                  'hf_5',
                  'hf_5a',
                  'hf_6',
                  'hf_6a',
                  'hf_7',
                  'hf_7a',
                  'hf_coordinator_comments',
                  # School Progress Report
                  'sch_school_name',
                  'sch_student_name',
                  'sch_1a',
                  'sch_1b',
                  'sch_2',
                  'sch_2a',
                  'sch_3',
                  'sch_3a',
                  'sch_4',
                  'sch_4a',
                  'sch_4b',
                  'sch_4c',
                  'sch_5',
                  'sch_5a',
                  'sch_6',
                  'sch_classes_grades',
                  'photo_main',
                  'is_complete',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_posted = timezone.now()
            post.save()
            messages.error(request, 'Must Upload photo to save.')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'survey/post_form.html', {'form': form})

def updateTask(request, pk):
	post = Post.objects.get(pk=pk)

	form = PostForm(instance=post)

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			form.save()
			return redirect('dashboard')

	context = {'form':form}

	return render(request, 'survey/update_task.html', context)

@login_required
def post_receipt(request, pk):
    post = get_object_or_404(Post, pk=pk)
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = "inline; filename={date}-{name}-post-receipt.pdf".format(
        date=post.date_posted.strftime('%Y-%m-%d'),
        name=slugify(post.coordinator),
    )
    html = render_to_string("survey/receipt_pdf.html", {
        'post': post,
    })

    font_config = FontConfiguration()
    HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response, font_config=font_config)
    return response

class HtmlPdf(FPDF, HTMLMixin):
    pass

def print_pdf(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user) 
    pdf = HtmlPdf()
    pdf.add_page()
    pdf.write_html(render_to_string('survey/pdf.html'))

    response = HttpResponse(pdf.output(dest='S').encode('latin-1'))
    response['Content-Type'] = 'application/pdf'

    return response
# def print_pdf(request):    
#     pdf = HtmlPdf()
#     pdf.add_page()
#     pdf.write_html(render_to_string('survey/pdf.html'))

#     response = HttpResponse(pdf.output(dest='S').encode('latin-1'))
#     response['Content-Type'] = 'application/pdf'

#     return response

class PostDetailView(DetailView):
    model = Post

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'survey/post_detail.html', {'post': post})

# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.date_posted = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'survey/post_edit.html', {'post': post})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    context = {
        'post': post
    }
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_posted = timezone.now()
            post.save()
            return redirect('post_detail', pk='pk')
    else:
        form = PostForm(instance=post)
    context = {
        'post': post,
        'form': form
    }
    return render(request, 'survey/post_edit.html', {'post': post})

# def post_edit(request, pk):
#     title = 'Update'
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(
#         request.POST or None,
#         request.FILES or None,
#         instance=post)
    
#     if request.method == "POST":
#         if form.is_valid():
#             form.instance.author = author
#             form.save()
#             return redirect(reverse("post-detail", kwargs={
#                 'pk': form.instance.pk
#             }))
#     context = {
#         'post': post,
#         'form': form
#     }
#     return render(request, "survey/post_edit.html", context)

# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=post_id)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post_id)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'survey/post_edit.html', {'form': form})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['coordinator',
                  'date_of_contact',
                  'student_surname',
                  'hostfamily',
                  'student_eng_name',
                  'st_1',
                  'st_1a',
                  'st_2',
                  'st_3',
                  'st_4',
                  'st_4a',
                  'st_4b',
                  'st_5',
                  'st_5a',
                  'st_6',
                  'st_6a',
                  'st_6b',
                  'st_7',
                  'st_7a',
                  'st_7b',
                  'st_coordinator_comments',
                  # Host Family Progress Report
                  'hf_hostfamily_name',
                  'hf_1',
                  'hf_1a',
                  'hf_2',
                  'hf_3',
                  'hf_3a',
                  'hf_3b',
                  'hf_4',
                  'hf_4a',
                  'hf_4b',
                  'hf_5',
                  'hf_5a',
                  'hf_6',
                  'hf_6a',
                  'hf_7',
                  'hf_7a',
                  'hf_coordinator_comments',
                  # School Progress Report
                  'sch_school_name',
                  'sch_student_name',
                  'sch_1a',
                  'sch_1b',
                  'sch_2',
                  'sch_2a',
                  'sch_3',
                  'sch_3a',
                  'sch_4',
                  'sch_4a',
                  'sch_4b',
                  'sch_4c',
                  'sch_5',
                  'sch_5a',
                  'sch_6',
                  'sch_classes_grades',
                  'photo_main',
                  'is_complete',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class HtmlPdf(FPDF, HTMLMixin):
    pass


def print_pdf(request):    
    pdf = HtmlPdf()
    pdf.add_page()
    pdf.write_html(render_to_string('survey/pdf.html'))

    response = HttpResponse(pdf.output(dest='S').encode('latin-1'))
    response['Content-Type'] = 'application/pdf'

    return response

