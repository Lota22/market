# from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name= 'contact'),
    path('categories', views.categories, name='categories'),
    path('category/<str:id>/<slug:slug>', views.category, name='category'),
    path('product/', views.product , name='product'),
    path('details/<str:id>/', views.details, name='details'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('password/', views.password, name='password'),
    path('cart/', views.cart, name = 'cart'),
    path('shopcart/', views.shopcart, name = 'shopcart'),
    path('delete/', views.deleteitem, name = 'deleteitem'),
    path('change/', views.change, name = 'change'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('pay/', views.pay, name = 'pay'),
    path('callback/', views.callback, name='callback'),
    path('search/', views.search, name='search'),
    path('history/', views.history, name='history'),
]
