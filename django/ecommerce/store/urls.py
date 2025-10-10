from django.urls import path
from.import views
from store.controller import authview, cart, wishlist, checkout, order
from django.contrib.auth import views as auth_views
from .forms import MyPasswordResetForm, MysetPasswordForm

urlpatterns = [
    path('',views.home,name="home"),
    path('Collections',views.Collections,name="Collections"),
    path('Collections/<str:slug>',views.collectionsview,name="collectionsview"),
    path('Collections/<str:cate_slug>/<str:prod_slug>',views.productview,name="productview"),
    path('product-list',views.productlistAjax),
    path('searchproduct',views.searchproduct,name="searchproduct"),
    path('registration/',views.register,name="customerregistration"),
    path('login/', views.loginpage, name="loginpage"),
    path('logout/', views.logoutpage, name="logout"),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='store/auth/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='store/auth/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='store/auth/password_reset_confirm.html', form_class=MysetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='store/auth/password_reset_complete.html'),name='password_reset_complete'),
    path('add-to-cart', cart.addtocart, name="addtocart"),
    path('cart', cart.viewcart, name="cart"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('delete-cart-item', cart.deletecartitem, name="deletecartitem"),
    path('wishlist', wishlist.index, name="wishlist"),
    path('add-to-wishlist', wishlist.addtowishlist, name="addtowishlist"),
    path('delete-wishlist-item', wishlist.deletewishlistitem, name="deletewishlistitem"),
    path('checkout',checkout.index,name="checkout"),
    path('place-order',checkout.placeorder,name="placeorder"),
    path('proceed-to-pay',checkout.razorpaycheck),
    path('my-orders',order.index, name="myorders"),
    path('view-order/<str:t_no>',order.vieworder, name="orderview"),
]