from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.views.generic import DetailView, RedirectView, UpdateView

from .serializers import UserSerializer

from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

class UserList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users/User_list.html'

    def get(self, request):
        queryset = User.objects.all()
        return Response({'Users': queryset})
    


class UserDetail(APIView):
    model = User
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users/user_detail.html'

    def get(self, request, id):
        if id:
            data = get_object_or_404(User, pk=id)
            print(data)
            serializer = UserSerializer(data)
            return Response({'serializer': serializer, 'data': data})
        # else:
        #     serializer = UserSerializer()
        #     return Response({'serializer': serializer})

    # def post(self, request, pk):
    #     if pk:
    #         data = get_object_or_404(data, pk=pk)
    #         serializer = UserSerializer(data, data=request.data)
    #         if not serializer.is_valid():
    #             return Response({'serializer': serializer, 'data': data})
    #         serializer.save()
    #     else:
    #         serializer = UserSerializer(data=request.data)
    #         serializer.save()

    #     return redirect('../../licsoftware/')