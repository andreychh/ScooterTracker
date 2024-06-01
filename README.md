> [!TIP]
> Подробную информацию о доступных запросах и ответах, а также примеры использования, можно найти
> в [/docs/api](docs/api.md).

## Содержание

* [Содержание](#содержание)
* [О проекте](#о-проекте)
    * [Описание](#описание)
    * [Технологии](#технологии)
* [Использование](#использование)
* [Авторы](#авторы)

## О проекте

### Описание

ScooterTracker — это приложение для отслеживания данных об электросамокатах. Пользователь может создавать новые
самокаты, изменять их модель и состояние, а также получать последние данные о заряде и координатах. Кроме того,
пользователь может запросить историю изменения этих параметров.

Обратите внимание, что данные о заряде и координатах генерируются отдельно. Приложение включает в себя функционал для
получения и обработки этих данных.

Проект выполнен в рамках зачетной работы по дисциплине "Технологии Интернета вещей" студентами ННГУ.

### Технологии

- **Язык программирования**: Python 3.12.3
- **Веб-фреймворк**: Flask
- **ORM**: SQLAlchemy
- **API Development**: Postman

## Использование

Для запуска приложения выполните следующие шаги:

1. Установите необходимые зависимости
    ```shell
    pip install -r requirements.txt
    ```
2. Создайте файл `.env` в корневой папке проекта и заполните его данными согласно `.env.example` или выполните команду:
    ```shell
    cp .env.example .env
    ```
3. Запустите приложение
    ```shell
    python -m app
    ```
4. Запустите генерацию данных (Опционально)
    ```shell
    python -m data_generation
    ```

Приложение будет доступно по адресу http://127.0.0.1:5000/.

## Авторы

- Черных Андрей
- Соцков Андрей
- Сарафанов Максим
- Казунин Никита
- Баярценгел Цэнд-Ауюш
- Круглов Григорий