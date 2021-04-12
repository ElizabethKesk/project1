from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [ 
    path('', include('Med.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
