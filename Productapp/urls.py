from rest_framework.routers import SimpleRouter
from .views import ProductOperations
simpleRouter = SimpleRouter()
simpleRouter.register('product',ProductOperations)
urlpatterns = simpleRouter.urls