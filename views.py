from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView



def get(self, request):
    w = User.objects.all()
    return Response({'posts': UserSerializer(w, many=True).data})
    
def post(self, request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    
    return Response({'post': serializer.data})

def put(self, request, *args, **kwargs):
    pk = kwargs.get("pk", None)
    if not pk:
        return Response({"error": "Method PUT not allowed"})
    
    try:
        instance = Women.objects.get(pk=pk)
    except:
        return Response({"error": "Object does not exists"})

    serializer = UserSerializer(data=request.data, instance=instance)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"post": serializer.data})

from rest_framework.pagination import PageNumberPagination

class UserAPIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000 #только для параметра page_size
    
class UserAPIList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserAPIListPagination
    
class UserAPIUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'put']
    
class UserAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

#Вьюсеты и модел вьюсеты вместо всего вон того ^
viewsets.ReadOnlyModelViewSet - только читать
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
#можно удалить миксины не нужные
class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
#переопределить маршруты
from rest_framework.viewsets import GenericViewSet

class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    #переопределение gqueryset тогда надо убрать выше queryset = User.objects.all()
    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return User.objects.all()[:3]
        return User.objects.filter(pk=pk)
    
    @action(methods=['get'], detail=False)   #detail=True - одна запись
    def category(self, request):
        cats = Category.objects.all()
        return Response({'cats': [c.name for c in cats]}) #появится новый маршрут women/category
    
    @action(methods=['get'], detail=True)   #detail=True - одна запись
    def category(self, requestm pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name}) #появится новый маршрут women/1/category для определённой категории

#тогда
path('Authentication/SignUp/', UserViewSet.as_view({'get': 'list'})),
path('Authentication/SignUp/', UserViewSet.as_view({'put': 'update'})),
path('Authentication/SignUp/', UserViewSet.as_view({'post': 'create'})),
path('Authentication/SignUp/', UserViewSet.as_view({'delete': 'destroy'})),

#нестандартное поведение роутеры

from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter
router.register(r'women', UserViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]

#т.е по маршруту api/v1/women (по такому же url) можно делать и пост запрос и гет
#т.е по маршруту api/v1/women/pk (по такому же url) можно делать и пат запрос и делит