from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.get_all_rooms, name='rooms'),
    path('get_room/<int:room_id>', views.get_room, name='get_room'),
    path('put_room', views.put_room, name='put_room'),
    path('delete_room/<int:room_id>', views.delete_room, name='delete_room'),
    path('patch_room/<int:room_id>', views.patch_room, name='patch_room'),
    path('put_ip/<int:ip_id>', views.put_ip, name='put_ip'),
    path('delete_ip/<int:room_id>/<int:ip_id>', views.delete_ip, name='delete_ip'),
    path('put_schedule/<int:room_id>', views.put_schedule, name='put_schedule'),
    path('patch_schedule/<int:room_id>/<int:climate_schedule_id>', views.patch_schedule, name='patch_schedule'),
    path('delete_schedule/<int:room_id>/<int:climate_schedule_id>', views.delete_schedule, name='delete_schedule'),
    path('put_climate/<int:room_id>', views.put_climate, name='put_climate'),
    path('patch_climate/<int:room_id>/<int:climate_id>', views.patch_climate, name='patch_climate'),
    path('delete_climate/<int:room_id>/<int:climate_id>', views.delete_climate, name='delete_climate'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
