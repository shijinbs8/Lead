from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('index/',views.index,name='index'),
    path('classroom/<int:classroom_id>/', views.bulb_control, name='bulb_control'),
    path('classroom/<int:classroom_id>/bulb/<int:bulb_id>/', views.update_pin, name='update_pin'),
    path('classroom/<int:classroom_id>/status/', views.get_status, name='get_status'),

]