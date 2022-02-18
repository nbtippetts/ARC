from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path('', views.schedule, name='schedule'),
    # path('', views.get_schedule, name='schedule'),
    # path('put_schedule/<int:room_id>', views.put_schedule, name='put_schedule'),
    # path('patch_schedule/<int:room_id>/<int:climate_schedule_id>', views.patch_schedule, name='patch_schedule'),
    # path('delete_schedule/<int:room_id>/<int:climate_schedule_id>', views.delete_schedule, name='delete_schedule'),
    # path('update_schedule', views.update_schedule, name='update_schedule'),
    # path('remove_schedule_view', views.remove_schedule_view, name='remove_schedule_view'),
    path('relay_on_off', views.relay_on_off, name='relay_on_off'),
    path('start_automation', views.start_automation, name='start_automation'),
    # path('update_app', views.update_app, name='update_app'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
