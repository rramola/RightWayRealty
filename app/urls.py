from django.urls import path
from . import views
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),
    # path('add_property/', views.add_property, name='add_property'),
    path("home/", views.home_page, name="home"),
    # re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    # re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path("maps/", views.googlemaps_view, name="googlemaps"),
    path("contact/", views.contact_page, name="contact")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)