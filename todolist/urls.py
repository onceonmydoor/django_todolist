
from django.urls import path,include
from . import views

app_name ="todolist"
#app_name是给app起名防止和其他app的网址名重合
urlpatterns = [
    path('home/',views.home,name="主页"),
    #name是给网址起名，方便更改
    path('about/',views.about,name="关于"),
    path('edit/<eachthing_id>',views.edit,name="编辑"),
    path('del/<eachthing_id>',views.delete,name="删除"),
    path('cross/<eachthing_id>',views.cross,name="划掉"),
]