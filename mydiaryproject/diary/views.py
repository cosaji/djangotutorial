from django.urls import reverse_lazy
from django.views.generic import TemplateView

class IndexView(TemplateView):
	template_name = 'index.html'

class DiaryCreateView(CreateView):
	template_name = 'diary_create.html'
	form_class = DiaryForm
	success_url = reverse_lazy('diary:diary_create_complete')

class DiaryCreateCompleteView(TemplateView):
	template_name = 'diary_create_complete.html'