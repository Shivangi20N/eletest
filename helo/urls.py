from django.contrib import admin
from django.urls import path , include
from home import views
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static



urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path("", views.index, name= 'home'),
  
    path('profile/',views.profile, name= 'profile' ),
    
    path('content_management/',views.content_management, name= 'content_management' ),
    path('demand/',views.demand, name= 'demand' ),
    path('sub/',views.sub, name= 'sub' ),
    path('service/',views.service, name= 'service'), 
    path('provider/',views.provider, name= 'provider'),
    path('add/',views.add, name= 'add'),
    path('view/',views.Service_View, name= 'view'),
    path('notification/',views.notification, name= 'notification'),
    path('driver/',views.driver, name= 'driver'),
    path('add_driver/',views.add_driver, name= 'add_driver'),
    path('location_view/',views.location_view, name= 'location_view'),
    path('map_view/',views.map_view, name= 'map_view'),
    path('agent_view/',views.agent_view, name= 'agent_view'),
    path('charges_view/',views.charges_view, name= 'charges_view'),
    path('add_customer/',views.add_customer, name= 'add_customer'),
    path('view_customer/',views.view_customer, name= 'view_customer'),
    path('order_view/',views.order_view, name= 'order_view'),
    path('dispatcher_new/',views.dispatcher_new, name= 'dispatcher_new'),
    path('dispatcher_live/',views.dispatcher_live, name= 'dispatcher_live'),
    path('dispatcher_completed/',views.dispatcher_completed, name= 'dispatcher_completed'),
    path('dispatcher_cancelled/',views.dispatcher_cancelled, name= 'dispatcher_cancelled'),
    path('add_agency/',views.add_agency, name= 'add_agency'),
    path('view_agency/',views.view_agency, name= 'view_agency'),
   
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
