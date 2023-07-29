from django.urls import path
from . import views

urlpatterns = [
    # path("",views.index,name="shopHome"),
    # path("addToCart/<str:id>",views.cartdb,name='addToCart'),
    # path("productview/addToCart/<str:id>",views.cartdb,name='addToCart'),
    # path("productview/cartproducts",views.viewCart,name='cartproducts'),
    # path("productview/<str:id>",views.prodView,name="ProductViewPage"),
    # path("cartproducts",views.viewCart,name='cartproducts'),
    # path("about/cartproducts",views.viewCart,name='cartproducts'),
    # path("about/",views.about,name="AboutUs"),
    # path("productview/about/",views.about,name="AboutUs"),

# -------------------------NOT MUCH IMPORTANT URLS ---------------------------------------

    # path("contact/",views.contact,name="ContactUs"),
    # path("tracker/",views.tracker,name="TrackingStatus"),
    # path("search/",views.search,name="search"),
    # path("checkout/",views.checkout,name="Checkout"),


# --------------------------Retrying to write correct urls ----------------------------------

    path("",views.index, name='home'),
    path("cartproducts",views.viewCart,name="viewcart"),
    path("addToCart/<str:id>",views.cartdb,name='addToCart'),
    path("about",views.about, name='AboutUs'),
    path("productview/cartproducts",views.viewCart,name='cartproducts'),
    path("productview/about",views.about,name="AboutUs"),
    path("productview/<str:id>",views.prodView,name="ProductViewPage"),
    path("productview/addToCart/<str:id>",views.cartdb,name='addToCart'),
    path("productview/remove/<str:id>",views.remove),
    path("remove/<str:id>",views.remove),
]
