from django.urls import path
from.views import *

urlpatterns=[
    path('chome',CustHomeView.as_view(),name="ch"),
    path('prodet/<int:pid>',ProductDetailView.as_view(),name="pdt"),
    path('acart/<int:pid>',addcart,name="acart"),
    path('viewcart',CartListView.as_view(),name="vcart"),
    path('delcart/<int:id>',deletecartitem,name="dcart"),
    path('check/<int:cid>',CheckOutView.as_view(),name="chckout"),
    path('orders',OrderView.as_view(),name="order"),
    path('cancelorder/<int:id>',cancel_order,name="orderc")
]