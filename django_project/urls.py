from django.contrib import admin
from django.urls import path
from appdomarcelo import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('jogos/update/<id>', views.update_jogo),
    path('jogos', views.create_jogo),
    path('extras', views.create_extra),
    path('extras/update/<int:id>/', views.update_extra, name='update_extra'),
    path('jogos/delete/<int:id>/', views.delete_jogo, name="delete_jogo"),
    path('extras/delete/<int:id>/', views.delete_rejogo, name="delete_extra"),
    path('register/', views.register, name='register'), 
    path('login/', views.user_login, name='user_login'),  
    path('logout/', views.user_logout, name='user_logout'), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
