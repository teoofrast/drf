from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Watch, BasketItem, Manufacturer
from .serializers import ProductSerializer, BasketItemSerializer, ManufacturerSerializer


class WatchAPIViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Представление API для отображения часов.

    Данное представление предоставляет следующие возможности:
    - Получение списка всех часов (`list()` метод)
    - Получение информации о конкретном часе (`retrieve()` метод)
    - Фильтрация часов по полю `name` с помощью параметра `search`
    - Сортировка часов по полям `name` и `price` с помощью параметра `ordering`

    Атрибуты:
    - queryset (QuerySet): Queryset с объектами часов.
    - serializer_class (serializers.Serializer): Сериализатор для преобразования объектов часов в JSON.
    - filter_backends (list): Список бэкендов фильтрации.
    - search_fields (list): Список полей для поиска.
    - ordering_fields (list): Список полей для сортировки.

    Примеры использования:
    - Получение списка всех часов: GET /watches/
    - Получение информации о часах с ID=1: GET /watches/1/
    - Поиск часов по названию 'Apple': GET /watches/?search=Apple
    - Сортировка часов по названию по возрастанию: GET /watches/?ordering=name
    - Сортировка часов по цене по убыванию: GET /watches/?ordering=-price
    """
    queryset = Watch.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'price']


class ManufacturerViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления производителями часов.

    Выдает все часы по одному производителю.

    Атрибуты:
    - queryset: Набор всех объектов модели `Manufacturer`.
    - serializer_class: Сериализатор, используемый для модели `Manufacturer`.

    Методы:
    - watches(self, request, pk=None):
        Возвращает список всех часов, принадлежащих производителю с указанным `pk`.

        Аргументы:
            request: Объект HTTP-запроса.
            pk: Первичный ключ производителя.

        Возвращает:
                Response: Ответ с данными о часах производителя.
    """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

    @action(detail=True, methods=['get'])
    def watches(self, request, pk=None):
        manufacturer = self.get_object()
        watches = manufacturer.watches.all()
        serializer = ProductSerializer(watches, many=True)
        manufacturer_data = {
            'name': manufacturer.name,
            'watches': serializer.data
        }
        return Response(manufacturer_data)


class AddToCart(viewsets.ModelViewSet):
    """
    Представление API для добавления товаров в корзину.

    Данное представление предоставляет следующие возможности:
    - Добавление товара в корзину (`create()` метод)

    Атрибуты:
    - queryset (QuerySet): Queryset с объектами элементов корзины.
    - serializer_class (serializers.Serializer): Сериализатор для преобразования объектов элементов корзины в JSON.

    Методы:
    - create(request, *args, **kwargs): Метод для добавления товара в корзину.
        - Принимает данные запроса в теле.
        - Валидирует данные с помощью сериализатора.
        - Сохраняет новый элемент корзины.
        - Возвращает ответ с сообщением о добавлении товара в корзину.

    Примеры использования:
    - Добавление товара в корзину: POST /add_to_cart/
        - Тело запроса: {"product": 1, "quantity": 2}
        - Ответ: {"Status": "Item was added to cart"}
    """
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'Status': 'Item was added to cart'})
