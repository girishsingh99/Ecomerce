from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Product Operations API')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/',include('rest_framework.urls')),
    path('v1/', include('Productapp.urls')),
    url(r'^$',schema_view)
]
