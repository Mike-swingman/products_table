## Описание

Этот проект представляет собой API для получения списка категорий блюд и связанных с ними опубликованных блюд.
Проект использует Django и Django REST framework.

## Модели

_FoodCategory_

* name_ru: Название на русском
* name_en: Название на английском
* name_ch: Название на китайском
* order_id: Порядковый номер

_Food_


* category: Категория продукта
* is_vegan: Вегетарианское меню
* is_special: Специальное предложение
* code: Код поставщика
* internal_code: Код в приложении
* name_ru: Название на русском
* description_ru: Описание на русском
* description_en: Описание на английском
* description_ch: Описание на китайском
* cost: Цена
* is_publish: Опубликовано
* additional: Дополнительные товары

## Использование
Получение списка категорий блюд с опубликованными блюдами

URL: /api/v1/foods/

Метод: GET

Пример ответа: 
```
[
      {
         "id":1,
         "name_ru":"Напитки",
         "name_en":null,
         "name_ch":null,
         "order_id":10,
         "foods":[
            {
               "internal_code":100,
               "code":1,
               "name_ru":"Чай",
               "description_ru":"Чай 100 гр",
               "description_en":null,
               "description_ch":null,
               "is_vegan":false,
               "is_special":false,
               "cost":"123.00",
               "additional":[
                  200
               ]
            },
            {
               "internal_code":200,
               "code":2,
               "name_ru":"Кола",
               "description_ru":"Кола",
               "description_en":null,
               "description_ch":null,
               "is_vegan":false,
               "is_special":false,
               "cost":"123.00",
               "additional":[
                  
               ]
            },
            {
               "internal_code":300,
               "code":3,
               "name_ru":"Спрайт",
               "description_ru":"Спрайт",
               "description_en":null,
               "description_ch":null,
               "is_vegan":false,
               "is_special":false,
               "cost":"123.00",
               "additional":[
                  
               ]
            },
            {
               "internal_code":400,
               "code":4,
               "name_ru":"Байкал",
               "description_ru":"Байкал",
               "description_en":null,
               "description_ch":null,
               "is_vegan":false,
               "is_special":false,
               "cost":"123.00",
               "additional":[
                  
               ]
            }
         ]
      },
      {
         "id":2,
         "name_ru":"Выпечка",
         "name_en":null,
         "name_ch":null,
         "order_id":20,
         "foods":[...]
      },
      {...},
      {...}
   ]
```