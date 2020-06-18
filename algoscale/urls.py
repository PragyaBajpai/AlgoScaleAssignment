from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from algo import views as algo_views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', algo_views.signup, name='signup'),
    path('', algo_views.login_view,name='user-login'),
    # path('', TemplateView.as_view(template_name="algo/listview.html"),name='home'),
    path('', include('django.contrib.auth.urls')),
    path('profile/<int:pk>/',algo_views.UserDetail.as_view(),name='profile'),
    path('user-list/',algo_views.UserListView.as_view(),name='Dashboard'),
    #url(r'^logout/$', algo_views.logout, {'template_name': 'registration/logged_out.html'}, name='logout'),

]