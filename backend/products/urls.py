from django.urls import path

from .views import ProductHome, UserGet, ProductDetailAPIView, ProductCreateAPIView, ProductListAPIVeiw, \
    ProductDeleteAPIView, ProductUpdateAPIView, ListMixinAPIView

app_name = 'products'
urlpatterns = [
    path('', ProductHome.as_view(), name='home'),
    path('user/', UserGet.as_view(), name='user_get'),
    path('<int:pk>', ProductDetailAPIView.as_view(), name='detail'),
    path('create/', ProductCreateAPIView.as_view(), name='create'),
    path('all/', ProductListAPIVeiw.as_view(), name='all'),
    path('<int:pk>/delete/', ProductDeleteAPIView.as_view(), name='delete'),
    path('<int:pk>/update/', ProductUpdateAPIView.as_view(), name='update'),
    path('mixins/list', ListMixinAPIView.as_view(), name='mixin_list'),
    path('mixins/<int:pk>/detail', ListMixinAPIView.as_view(), name='mixin_detail'),
    path('mixins/<int:pk>/delete', ListMixinAPIView.as_view(), name='mixin_delete'),
    path('mixins/create/', ListMixinAPIView.as_view(), name='mixin_create'),
]
