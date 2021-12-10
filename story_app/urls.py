from django.urls import path
from story_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('registration',views.registration,name='registration'),
    path('story',views.story,name='story'),
    path('crstory',views.crstory,name='crstory'),
    path('updatestory/<int:id>/',views.story_update, name="updatestory"),
    path('deletestory/<int:id>/',views.story_delete, name="deletestory"),
    path('logout', views.logout, name='logout')

]