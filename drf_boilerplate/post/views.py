from django.views.generic import ListView
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
from rest_framework.response import Response
from rest_framework.settings import api_settings

from post.models import Post, Comment
from post.paginations import PostPagination
from post.serializers import PostSerializer, PostVerySecretSerializer, CommentSerializer
from utils.decorators import paginate


class PostModelViewSet(viewsets.ModelViewSet):
    """
    viewset 작성 시 절대! ModelViewSet 을 쓰지 않는 것이 좋습니다.
    ModelViewSet 은 단순히 아래의 예시처럼 GenericViewSet 에 모든 mixin 들을 상속한 class 인데,
    쓸데없이 추가된 기능은 각 기능별 authentication 을 정해주지 않으면 보안 상 취약점이 될 뿐입니다.
    """
    pass


class PostViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination

    def get_queryset(self):
        self.queryset.order_by('id')
        query_params = self.request.query_params
        """
        get queryset 사용 시 주의점
        1. self.queryset 으로 가져오지 말고 model_class.objects 로 queryset 을 한번 더 call 해주기
        안그러면 이 viewset 이 불려온 시점에서 memory 에 queryset 으로 저장 된 값이 가져와집니다.
        그 사이에 database 에 변화가 있어도 self.queryset 을 사용하면 감지가 안되겠죠?
        """
        return Post.objects.filter()

    # def get_serializer_class(self):
    #     # """
    #     # action 에 따라 사용 할 serializer 를 불러오는 함수입니다.
    #     # """
    #     # if self.action == 'list':
    #     #     return PostSerializer
    #     # elif self.action == 'retrieve':
    #     #     return PostVerySecretSerializer
    #     # elif self.request.user.is_admin:
    #     #     # return something else
    #     #     pass
    #     # ...
    #     return None


    """
    viewset 에 기본적으로 추가할 수 있는 5개의 action 들의 source code 입니다.
    길이가 길지 않지만 중요한 내용들을 다루고 있고, 자주 override 해야하는 함수들 이므로 한번 씩 읽어보시는 것이 좋을 것 같습니다.
    list : GET /api/v1/post/
    retrieve : GET /api/v1/post/{pk}/
    create : POST /api/v1/post/
    update : PUT/PATCH /api/v1/post/{pk}/
    destroy : DELETE /api/v1/post/{pk}/
    not-detail action : ANY /api/v1/post/do-something-on-list/ (url_path 를 설정한 경우)
    detail action : ANY /api/v1/post/{pk}/do_something_on_detail/ (url_path 를 설정하지 않은 경우 함수 이름 그대로)
    """
    # ListModelMixin
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # RetrieveModelMixin
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # CreateModelMixin
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    # UpdateModelMixin
    def update(self, request, *args, **kwargs):

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    # DestroyModelMixin
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

    # 위의 5가지 외에 추가 action 들은 action decorator 를 이용하여 추가합니다.
    @action(detail=False, url_path=r'^do-something-on-list/$')
    def do_something_on_list(self, request):
        pass

    @action(detail=False)
    def get_answer_detail(self, request, *kwargs):
        pk = kwargs.get('pk')

    @action(
        detail=True,
        serializer_class=PostVerySecretSerializer,  #사용할 serializer_class 를 설정할 수 있습니다.
        methods=['GET', 'POST', 'PATCH']  # default 가 GET 이고 필요할 경우 추가해주시면 됩니다.
    )
    def do_something_on_detail(self, request, *args, **kwargs):
        if self.request.method == 'GET':
            pass
        elif self.request.method == 'POST':
            pass
        else:
            pass

    @action(detail=True, serializer_class=CommentSerializer)
    def comment(self, request, *args, **kwargs):
        post_id = kwargs.get('pk', None)
        queryset = Comment.objects.filter(post_id=post_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post.html'


class CommentViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
