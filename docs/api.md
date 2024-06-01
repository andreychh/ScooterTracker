## Содержание

* [Содержание](#содержание)
* [Объекты](#объекты)
    * [ChargeData](#chargedata)
    * [PositionData](#positiondata)
    * [Scooter](#scooter)
* [Запросы](#запросы)
    * [Добавление самоката](#добавление-самоката)
    * [Удаление самоката](#удаление-самоката)
    * [Получение самоката](#получение-самоката)
    * [Получение активных самокатов](#получение-активных-самокатов)
    * [Получение данных о заряде самоката](#получение-данных-о-заряде-самоката)
    * [Получение данных о положении самоката](#получение-данных-о-положении-самоката)
    * [Получение модели самоката](#получение-модели-самоката)
    * [Обновление модели самоката](#обновление-модели-самоката)
    * [Получение состояния самоката](#получение-состояния-самоката)
    * [Обновление состояния самоката](#обновление-состояния-самоката)

## Объекты

### ChargeData

**Описание:**

Объект, представляющий данные о заряде самоката.

```text
{
    "charge": Float,
    "recorded_at": String
}
```

**Параметры:**

- `charge` (Float): Уровень заряда самоката в диапазоне от 0.0 до 1.0.
- `recorded_at` (String): Дата и время, когда были получены данные.

### PositionData

**Описание:**

Объект, представляющий данные о положении самоката.

```text
{
    "latitude": Float,
    "longitude": Float,
    "recorded_at": String
}
```

**Параметры:**

- `latitude` (Float): Широта положения самоката в диапазоне от -90.0 до 90.0.
- `longitude` (Float): Долгота положения самоката в диапазоне от -180.0 до 180.0.
- `recorded_at` (String): Дата и время, когда были получены данные.

### Scooter

**Описание:**

Объект, представляющий самокат.

```text
{
    "id": Integer,
    "model": String,
    "state": String,
    "charge_data": ChargeData | Null,
    "position_data": PositionData | Null
}
```

**Параметры:**

- `id` (Integer): Идентификатор самоката.
- `model` (String): Название модели самоката.
- `state` (String): Состояние самоката "Active" или "Inactive".
- `charge_data` ([ChargeData](#chargedata) | Null): Объект, представляющий данные о заряде самоката или Null, если
  данные отсутствуют.
- `position_data` ([PositionData](#positiondata) | Null): Объект, представляющий данные о положении самоката
  или Null, если данные отсутствуют.

## Запросы

### Добавление самоката

**Описание:**

Добавляет новый самокат.

**Запрос:**

```text
POST /scooters
{
    "model": String
    "state": String
}
```

**Параметры:**

- `model` (String): Название модели добавляемого самоката.
- `state` (String): Состояние добавляемого самоката "Active" или "Inactive", по умолчанию "Active".

**Ответ:**

- 201 Created: Самокат успешно создан.
    ```text
    {
        "id": Integer,
        "message": "Scooter created successfully"
    }
    ```
  Параметры:
    - `id` (Integer): Идентификатор добавленного самоката.


- 400 Bad Request: Некорректные данные в запросе.

**Пример:**

Запрос:

```shell
curl --location 'http://127.0.0.1:5000/scooters' \
--header 'Content-Type: application/json' \
--data '{
    "model": "modelA"
}'
```

Ответ:

```json
{
  "id": 1,
  "message": "Scooter created successfully"
}
```

### Удаление самоката

**Описание:**

Удаляет самокат. Все данные, связанные с этим самокатом, также будут удалены.

**Запрос:**

```text
DELETE /scooters/<id: Integer>
```

**Параметры:**

- `id` (Integer): Идентификатор удаляемого самоката.

**Ответ:**

- 200 OK: Самокат успешно удален.
  ```text
  {
    "message": "Scooter deleted successfully"
  }
  ```

- 404 Not Found: Самокат не найден.

**Пример:**

Запрос:

```shell
curl --location --request DELETE 'http://127.0.0.1:5000/scooters/1'
```

Ответ:

```json
{
  "message": "Scooter deleted successfully"
}
```

### Получение самоката

**Описание:**

Возвращает самокат.

**Запрос:**

```text
GET /scooters/<id: Integer>
```

**Параметры:**

- `id` (Integer): Идентификатор возвращаемого самоката.

**Ответ:**

- 200 OK: Запрос выполнен успешно.
  ```text
  scooter: Scooter
  ```
  Параметры:
    - `scooter` ([Scooter](#scooter)): Объект, представляющий самокат.


- 400 Bad Request: Некорректные данные в запросе.

**Пример:**

Запрос:

```shell
curl --location 'http://127.0.0.1:5000/scooters/1'
```

Ответ:

```json
{
  "charge_data": {
    "charge": 0.14837290965341576,
    "recorded_at": "Sat, 01 Jun 2024 09:22:47 GMT"
  },
  "id": 1,
  "model": "ModelB",
  "position_data": {
    "latitude": -69.67629161774954,
    "longitude": 62.67096369389451,
    "recorded_at": "Sat, 01 Jun 2024 09:22:45 GMT"
  },
  "state": "Active"
}
```

### Получение активных самокатов

**Описание:**

Возвращает список активных самокатов.

**Запрос:**

```text
GET /scooters/active
```

**Ответ:**

- 200 OK: Запрос выполнен успешно.
    ```text
    [
      scooter: Scooter,
      ...
    ]
    ```
  Параметры:
    - `scooter` ([`Scooter`](#scooter)): Объект, представляющий самокат.

**Пример:**

Запрос:

```shell
curl --location 'http://127.0.0.1:5000/scooters/active'
```

Ответ:

```json
[
  {
    "charge_data": {
      "charge": 0.13398888522589325,
      "recorded_at": "Sat, 01 Jun 2024 09:25:53 GMT"
    },
    "id": 1,
    "model": "ModelA",
    "position_data": {
      "latitude": -69.68489369466687,
      "longitude": 62.70364856171199,
      "recorded_at": "Sat, 01 Jun 2024 09:25:55 GMT"
    },
    "state": "Active"
  },
  {
    "charge_data": {
      "charge": 0.8465053884931114,
      "recorded_at": "Sat, 01 Jun 2024 09:25:53 GMT"
    },
    "id": 2,
    "model": "modelC",
    "position_data": {
      "latitude": 64.07187294016985,
      "longitude": 129.87581332512676,
      "recorded_at": "Sat, 01 Jun 2024 09:25:55 GMT"
    },
    "state": "Active"
  }
]
```

### Получение данных о заряде самоката

**Описание:**

Возвращает список данных о заряде самоката, отсортированный по убыванию даты и времени добавления данных.

**Запрос:**

```text
GET /scooters/<id: Integer>/charge?limit=<limit: Integer>
```

**Параметры:**

- `id` (Integer): Идентификатор самоката, данные которого необходимо получить.
- `limit` (Integer): Ограничение на количество записей.

**Ответ:**

- 200 OK: Запрос выполнен успешно.
  ```text
  [
    charge_data: ChargeData,
    ...
  ]
  ```
  Параметры:
    - `charge_data` ([`ChargeData`](#chargedata)): Объект, представляющий данные о заряде самоката.


- 404 Not Found: Данные не найдены.

**Пример:**

Запрос:

```shell
curl --location 'http://127.0.0.1:5000/scooters/1/charge?limit=3'
```

Ответ:

```json
{
  "charge_data": [
    {
      "charge": 0.11521077611355196,
      "recorded_at": "Sat, 01 Jun 2024 09:27:19 GMT"
    },
    {
      "charge": 0.20771469058526532,
      "recorded_at": "Sat, 01 Jun 2024 09:27:14 GMT"
    },
    {
      "charge": 0.30315837484413977,
      "recorded_at": "Sat, 01 Jun 2024 09:27:09 GMT"
    }
  ]
}
```

### Получение данных о положении самоката

**Описание:**

Возвращает список данных о положении самоката, отсортированный по убыванию даты и времени добавления данных.

**Запрос:**

```text
GET /scooters/<id: Integer>/position?limit=<limit: Integer>
```

Параметры:

- `id` (Integer): Идентификатор самоката, данные которого необходимо получить.
- `limit` (Integer): Ограничение на количество записей.

**Ответ:**

- 200 OK: Запрос выполнен успешно.
  ```text
  [
    position_data: PositionData,
    ...
  ]
  ```
  Параметры:
    - `position_data` ([`PositionData`](#positiondata)): Объект, представляющий данные о положении самоката.


- 404 Not Found: Данные не найдены.

**Пример:**

Запрос:

```shell
curl --location 'http://127.0.0.1:5000/scooters/2/position?limit=2'
```

Ответ:

```json
{
  "position_data": [
    {
      "latitude": 64.07327956193609,
      "longitude": 129.8678509974332,
      "recorded_at": "Sat, 01 Jun 2024 09:28:44 GMT"
    },
    {
      "latitude": 64.07089028318008,
      "longitude": 129.86492903934774,
      "recorded_at": "Sat, 01 Jun 2024 09:28:37 GMT"
    }
  ]
}
```

### Получение модели самоката

**Описание:**

Возвращает модель самоката.

**Запрос:**

```text
GET /scooters/<id: Integer>/model
```

Параметры:

- `id`: Идентификатор самоката, модель которого необходимо получить.

**Ответ:**

- 200 OK: Запрос выполнен успешно.
  ```text
  {
    "model": String
  }
  ```
  Параметры:
    - `model`: Название модели самоката.

- 404 Not Found: Данные не найдены.

**Пример:**

Запрос:

```shell
curl --location 'http://127.0.0.1:5000/scooters/1/model'
```

Ответ:

```json
{
  "model": "ModelA"
}
```

### Обновление модели самоката

**Описание:**

Обновляет состояние самоката.

**Запрос:**

```text
PUT /scooters/<id: Integer>/model
```

**Параметры:**

- `id` (Integer): Идентификатор самоката, модель которого необходимо обновить.

**Ответ:**

- 200 OK: Модель самоката обновлена успешно.
  ```text
  {
      "message": "Scooters model updated successfully"
  }
  ```

- 404 Not Found: Данные не найдены.

**Пример:**

Запрос:

```shell
curl --location --request PUT 'http://127.0.0.1:5000/scooters/1/model' \
--header 'Content-Type: application/json' \
--data '{
	"model": "ModelB"
}'
```

Ответ:

```json
{
  "message": "Scooters model updated successfully"
}
```

### Получение состояния самоката

**Описание:**

Возвращает состояние самоката.

**Запрос:**

```text
GET /scooters/<id: Integer>/state
```

**Параметры:**

- `id` (Integer): Идентификатор самоката, состояние которого необходимо получить.

**Ответ:**

- 200 OK: Запрос выполнен успешно.
  ```text
  {
      "state": String
  }
  ```
  Параметры:
    - `state` (String): Состояние самоката "Active" или "Inactive".

- 404 Not Found: Данные не найдены.

**Пример:**

Запрос:

```shell
curl --location 'http://127.0.0.1:5000/scooters/1/state'
```

Ответ:

```json
{
  "state": "Active"
}
```

### Обновление состояния самоката

**Описание:**

Обновляет состояние самоката.

**Запрос:**

```text
PUT /scooters/<id: Integer>/state
```

**Параметры:**

- `id` (Integer): Идентификатор самоката, состояние которого необходимо обновить.

**Ответ:**

- 200 OK: Состояние самоката обновлено успешно.
  ```text
  {
      "message": "Scooters state updated successfully"
  }
  ```


- 404 Not Found: Данные не найдены.

**Пример:**

Запрос:

```shell
curl --location --request PUT 'http://127.0.0.1:5000/scooters/1/state' \
--header 'Content-Type: application/json' \
--data '{
	"state": "Inactive"
}'
```

Ответ:

```json
{
  "message": "Scooters state updated successfully"
}
```
