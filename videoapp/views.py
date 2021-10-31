from django.contrib import messages
from django.db.models import Q

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from videoapp.models import Video

import csv

data = None
file_dir = 'static/'

def read_data(youtube):
    with open(file_dir + f'{youtube}.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        global data
        data = list(reader)
    return

def footer(youtube, Video, bulk_list):
    Video.objects.bulk_create(bulk_list)

    with open(file_dir + f'{youtube}.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
    return

def add_youtube(request):
    read_data('youtube')
    if not data:
        return HttpResponse('Nothing to update')

    arr = []
    for row in data:
        arr.append(Video(
            title=row[0],
            url=row[1],
            tags=row[2]
        ))
    footer('youtube', Video, arr)
    return HttpResponse('Youtube table update')

class VideoListView(ListView):
    model = Video
    context_object_name = 'video_list'
    template_name = 'videoapp/video_list.html'
    paginate_by = 8

    def get_queryset(self):

        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')
        video_list = Video.objects.order_by('-id')

        if search_keyword:
            if len(search_keyword) >= 1:
                if search_type == 'all':
                    search_video_list = video_list.filter(
                        Q(title__icontains=search_keyword))
                elif search_type == 'title':
                    search_video_list = video_list.filter(title__icontains=search_keyword)

                return search_video_list
            else:
                messages.error(self.request, '검색어는 1글자 이상 입력해주세요.')
        return video_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')

        if len(search_keyword) > 1:
            context['q'] = search_keyword
        context['type'] = search_type

        return context

class VideoDetailView(DetailView):
    model = Video
    context_object_name = 'target_video'
    template_name = 'videoapp/video_detail.html'
