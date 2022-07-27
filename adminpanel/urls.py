from django.urls import path
from django.views import View
from .import views

urlpatterns = [
    path('',views.adminpanel,name="adminpanel"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('user_accounts_table/',views.user_accounts_table,name="user_accounts_table"),
    path('cart_table/<int:id>',views.cart_table,name="cart_table"),
    path('category_table/<int:id>/',views.category_table,name="category_table"),
    path('order_table/<int:id>/',views.order_table,name='order_table'),
    path('store_table/<int:id>/',views.store_table,name="store_table"),

    path('ban_user/<int:id>/',views.ban_user,name="ban_user"),
    path('unban_user/<int:id>/',views.unban_user,name='unban_user'),
    
    path('add_main_category/',views.add_main_category,name="add_main_category"),
    path('edit_main_category/<int:id>/',views.edit_main_category,name="edit_main_category"),
    path('delete_main_category/<int:id>/',views.delete_main_category,name="delete_main_category"),

    path('add_category/',views.add_category,name="add_category"),
    path('edit_category/<int:id>/',views.edit_category,name="edit_category"),
    path('delete_category/<int:id>/',views.delete_category,name='delete_category'),

    path('add_sub_category/',views.add_sub_category,name="add_sub_category"),
    path('edit_sub_category/<int:id>/',views.edit_sub_category,name="edit_sub_category"),
    path('delete_sub_category/<int:id>/',views.delete_sub_category,name="delete_sub_category"),

    path('add_product/',views.add_product,name="add_product"),
    path('edit_product/<int:id>/',views.edit_product,name='edit_product'),
    path('delete_product/<int:id>/',views.delete_product,name="delete_product"),

    path('user_orders/<int:order_id>/', views.user_orders, name="user_orders"),
    


    
]
