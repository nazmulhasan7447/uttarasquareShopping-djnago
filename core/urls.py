from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^fe/index/$', views.fe_index, name='feIndex'),
    re_path(r'^$', views.fe_home, name="feHome"),
    re_path(r'^fe/store/directory/$', views.fe_storeDirectory, name="feStoreDirectory"),

    re_path(r'^fe/about/$', views.fe_about, name="feAbout"),
    re_path(r'^fe/book/appointment/$', views.fe_book_appontment, name="feBookAppointment"),
    re_path(r'^fe/contact/$', views.fe_contact, name="feContactUs"),

    re_path(r'^fe/event/list/$', views.fe_eventList, name="feEventList"),
    re_path(r'^fe/event/details/$', views.fe_eventDetails, name="feEventDetails"),
    re_path(r'^fe/restaurants/list/$', views.fe_restaurants, name="feRestaurants"),
    re_path(r'^fe/service/list/$', views.fe_service, name="feService"),
    re_path(r'^fe/shop/details/$', views.fe_shop_details, name="feShopDetials"),
    re_path(r'^fe/shop/$', views.fe_shop, name="feShop"),

    re_path(r'^fe/convention/hall/$', views.fe_convention_hall, name="feConventionHall"),

    re_path(r'^fe/floor/$', views.fe_floor, name="feFloor"),
    re_path(r'^fe/floor/details/(?P<pk>\d+)/$', views.fe_floor_details, name="feFloorDetails"),
]
