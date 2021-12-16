from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'^ap/index/$', views.ap_index, name="apIndex"),
    re_path(r'^ap/home/$', views.ap_home, name="apHome"),

    re_path(r'^ap/remove/user/(?P<pk>\d+)/$', views.ap_removeUser, name="apRemoveUser"),


    re_path(r'^ap/add/banner/$', views.ap_addBanner, name="apAddBanner"),
    re_path(r'^ap/del/banner/(?P<pk>\d+)/$', views.ap_delBanner, name="apDelBanner"),

    # event ***********************************************
    re_path(r'^ap/add/event/$', views.ap_addNew_Event, name="apAddNewEvent"),

    re_path(r'^ap/event/list/$', views.ap_EventList, name="apEventList"),

    re_path(r'^ap/add/store/$', views.ap_addNew_store, name='apAddNewStore'),
    re_path(r'^ap/store/list/$', views.ap_storeList, name="apStoreList"),

    re_path(r'^ap/add/restaurants/$', views.ap_addNew_restaurants, name='apAddNewRestaurants'),
    re_path(r'^ap/restaurants/list/$', views.ap_restauRantList, name='apRestaurantList'),


    # add site logo ############################################
    re_path(r'^ap/add/site/logo/$', views.ap_addSiteLogo, name="apAddSiteLogo"),

    # delete site logo
    re_path(r'^ap/del/site/logo/(?P<logo_id>\d+)/$', views.ap_delSiteLogo, name="apDelSiteLogo"),

    # edit site logo
    re_path(r'^ap/edit/site/logo/(?P<logo_id>\d+)/$', views.ap_editSiteLogo, name="apEditSiteLogo"),

    # site contact info
    re_path(r'^ap/add/site/contact/info/$', views.ap_addSiteContactInfo, name="apAddSiteContactInfo"),

    # site contact info
    re_path(r'^ap/add/site/contact/info/bangla/$', views.ap_addSiteContactInfoBangla, name="apAddSiteContactInfoBangla"),
    re_path(r'^ap/del/site/contact/info/bangla/(?P<pk>\d+)/$', views.ap_deleteSiteContactInfoBangla, name="apDeleteSiteContactInfoBangla"),
    re_path(r'^ap/edit/site/contact/info/bangla/(?P<pk>\d+)/$', views.ap_editSiteContactInfoBangla, name="apEditSiteContactInfoBangla"),

    # delete contact info
    re_path(r'^ap/del/site/contact/info/(?P<contact_id>\d+)/$', views.ap_delSiteContactInfo, name="apDelSiteContactInfo"),

    # edit contact info
    re_path(r'^ap/edit/site/contact/info/(?P<contact_id>\d+)/$', views.ap_editSiteContactInfo, name="apEditSiteContactInfo"),


    #  about us
    re_path(r'^ap/news/about/us/$', views.ap_aboutUs, name="apAboutUs"),
    re_path(r'^ap/del/news/about/us/(?P<pk>\d+)/$', views.ap_delAboutUs, name='apDelAboutUs'),
    re_path(r'^ap/del/news/about/us/edit/(?P<pk>\d+)/$', views.ap_editAboutUs, name='apEditAboutUs'),

    # msg list
    re_path(r'^ap/visitor/msg/list/$', views.ap_VisitorMsgList, name="apVisitorMessageList"),

    re_path(r'^ap/del/visitor/msg/(?P<pk>\d+)/$', views.ap_DelVisitorMsg, name="apDelVisitorMsg"),

    #************integrate social media link
    re_path(r'^ap/add/social/media/link/$', views.ap_addSocialMediaLink, name="apAddSocialMediaLink"),
    re_path(r'^ap/del/social/media/link/(?P<pk>\d+)/$', views.ap_delSocialMediaLink, name="apDelSocialMediaLink"),
    re_path(r'^ap/edit/social/media/link/(?P<pk>\d+)/$', views.ap_editSocialMediaLink, name="apEditSocialMediaLink"),


    # ********************************************
    re_path(r'^ap/add/appointment/img/$', views.ap_bookApointment, name="apAddBookAppointment"),
    re_path(r'^ap/del/appointment/img/(?P<pk>\d+)/$', views.ap_delBookAppointment, name="apDelBookAppointment"),


    re_path(r'^ap/booking/appointment/list/$', views.ap_bookingAppointmentList, name="apBookingAppointmentList"),
    re_path(r'^ap/booking/appointment/del/(?P<pk>\d+)/$', views.ap_delBookingRequest, name="apDelBookingAppointmentRequest"),

    re_path(r'^ap/add/floor/items/$', views.ap_addItems_toFloor, name="apAddItemsToFloor"),
    re_path(r'^ap/floor/items/list/$', views.ap_listItems_toFloor, name="apFloorItemsList"),


]
