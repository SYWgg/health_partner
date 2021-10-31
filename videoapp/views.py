from django.contrib import messages
from django.db.models import Q

from django.views.generic import DetailView, ListView

from videoapp.models import Video


class VideoListView(ListView):
    model = Video
    context_object_name = 'video_list'
    template_name = 'video_list.html'
    paginate_by = 8

    def get_queryset(self):

        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')
        video_list = Video.objects.order_by('-id')

        if search_keyword:
            if len(search_keyword) >= 1:
                if search_type == 'all':
                    search_video_list = video_list.filter(
                        Q(title__icontains=search_keyword) | Q(keyword__icontains=search_keyword))
                elif search_type == 'title':
                    search_video_list = video_list.filter(title__icontains=search_keyword)
                elif search_type == 'keyword':
                    search_video_list = video_list.filter(keyword__icontains=search_keyword)

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
    template_name = ''