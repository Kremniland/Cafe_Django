from django.urls import path

import acoffe.views as v


urlpatterns = [
    path('', v.home_page, name='home_page'),
    path('list/', v.list_coffe, name='list_coffe'),

    # ListView
    # path('list/', v.CoffeList.as_view(), name='list_coffe'),

    path('list/<int:coffe_id>/', v.detail_coffe, name='detail_coffe'),
]
