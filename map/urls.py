from django.urls import path , include
from . import views
# from communitygis.core import views as core_views


urlpatterns = [
	path('',views.front,name = 'front'),
    path('home/',views.home,name= 'home'),
    path('login/',views.login_user, name = 'login'),
    path('logout/',views.logout_user, name = 'logoutU'),
    path('signup/',views.signup_user, name = 'signup'),
    path('change_password/',views.change_password, name = 'changepass'),
    # path(r'^signup/$', core_views.signup, name='signup'),)

    path('demo/',views.demo,name='demo'),
    path('home/swm/',views.solidWasteManagement,name = 'swm'),
    path('home/census/',views.census,name = 'census'),
    path('home/iitbombay/',views.iitBombay,name = 'iit'),
    path('home/education/',views.education,name = 'edu'),
    path('test/',views.test,name = 'test'),
    path('home/health/',views.health,name = 'health'),
    path('home/water/',views.water,name = 'water'),

    path('uploadlayer/',views.upload_layers,name='upload_layers')



]