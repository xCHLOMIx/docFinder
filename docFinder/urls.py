from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', include('patients.urls')),
    path('doctors/', include('doctors.urls')),
    path('', include('base.urls'))
]
