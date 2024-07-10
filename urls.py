from django.contrib import admin
from django.urls import path, include
from users.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('users/', include('users.urls')),
    path('', include('users.urls')),
    path('', include('nys_tvtms.urls'))  
]
