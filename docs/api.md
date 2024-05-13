## Содержание

* [Содержание](#содержание)
* [Добавление самоката](#добавление-самоката)
* [Удаление самоката](#удаление-самоката)
* [Получение самоката](#получение-самоката)
* [Получение активных самокатов](#получение-активных-самокатов)

## Добавление самоката

**Описание:**

Добавляет новый самокат в систему.

**Запрос:**

```text
POST /scooters
{
  "model": str
  "state": "Active"|"Inactive" = "Active"
}
```

Параметры:

- `model` (строка): Название модели самоката.
- `state` (строка): Состояние самоката `Active` или `Inactive`, по умолчанию `Active`.

**Ответ:**

- 201 Created: Самокат успешно создан.
    ```json lines
    {
      "id": int,
      "message": "Scooter created successfully"
    }
    ```
  Параметры:
    - `id` (целое): идентификатор добавленного самоката.


- 400 Bad Request: Некорректные данные в запросе.

**Пример:**

```shell
curl --location 'http://127.0.0.1:5000/scooters' \
--header 'Content-Type: application/json' \
--data '{ "model": "SP-1000X" }'
```

```json
{
  "id": 1,
  "message": "Scooter created successfully"
}
```

## Удаление самоката

**Описание:**

Удаляет самокат из системы. Все данные, связанные с этим самокатом, также будут удалены.

**Запрос:**

```text
DELETE /scooters/<id: int>
```

Параметры:

- `id` (целое): идентификатор удаляемого самоката.

**Ответ:**

- 200 OK: Самокат успешно удален.
  ```json lines
  {
    "message": "Scooter deleted successfully"
  }
  ```

- 404 Not Found: Самокат не найден.

**Пример:**

```shell
curl --location --request DELETE 'http://127.0.0.1:5000/scooters/1'
```

```json
{
  "message": "Scooter deleted successfully"
}
```

## Получение самоката

**Описание:**

Возвращает информацию о самокате.

**Запрос:**

```text
GET /scooters/<id: int>
```

Параметры:

- `id` (целое): идентификатор удаляемого самоката.

**Ответ:**

- 200 OK: Запрос выполнен успешно.
  ```json lines
  {
    "id": int,
    "model": str,
    "state": state,
    "charge_data": object | null,
    "position_data": object | null
  }
  ```
  Параметры:
    - `id` (целое): Идентификатор самоката.
    - `model` (строка): Название модели самоката.
    - `state` (строка): Состояние самоката `Active` или `Inactive`.
    - `charge_data` (объект или null): Информация о заряде самоката.
    - `position_data` (объект или null): Информация о местоположении самоката.


- 400 Bad Request: Некорректные данные в запросе.

**Пример:**

```shell
curl --location 'http://127.0.0.1:5000/scooters/1'
```

```json
{
  "id": 1,
  "model": "SP-1000X",
  "state": "Active",
  "charge_data": {
    "charge": 0.4464277904972725,
    "recorded_at": "Mon, 13 May 2024 18:32:41 GMT"
  },
  "position_data": {
    "latitude": -58.38715395855737,
    "longitude": 73.82412575280411,
    "recorded_at": "Mon, 13 May 2024 18:27:11 GMT"
  }
}
```

## Получение активных самокатов

**Описание:**

Возвращает информацию о всех активных самокатах, включая данные об их заряде и текущем местоположении.

**Запрос:**

```text
GET /scooters/active
```

**Ответ:**

- 200 OK: Запрос выполнен успешно.
    ```json lines
    [
      {
        "id": int,
        "model": str,
        "state": "Active",
        "charge_data": object | null,
        "position_data": object | null
      },
      ... 
    ]
    ```
  Параметры:
    - `id` (целое): Идентификатор самоката.
    - `model` (строка): Название модели самоката.
    - `state` (строка): Состояние самоката `Active` или `Inactive`. В данном случае всегда `Active`.
    - `charge_data` (объект или null): Информация о заряде самоката.
    - `position_data` (объект или null): Информация о местоположении самоката.

**Пример:**

```shell
curl --location 'http://127.0.0.1:5000/scooters/active'
```

```json
[
  {
    "id": 1,
    "model": "SP-1000X",
    "state": "Active",
    "charge_data": {
      "charge": 0.4464277904972725,
      "recorded_at": "Mon, 13 May 2024 18:32:41 GMT"
    },
    "position_data": {
      "latitude": -58.38715395855737,
      "longitude": 73.82412575280411,
      "recorded_at": "Mon, 13 May 2024 18:27:11 GMT"
    }
  }
]
```

