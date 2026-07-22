# Контракт данных

## Вход

Telegram `message.document` с расширением:

- `.csv`
- `.xlsx`

CSV MVP использует разделитель `;`.

## Карта столбцов от AI

```json
{
  "sku_column": "Код поставщика",
  "name_column": "Наименование товара",
  "price_column": "Оптовая цена ₽",
  "stock_column": "Остаток",
  "unit_column": "Ед. изм.",
  "manufacturer_column": "Производитель",
  "currency": "RUB",
  "confidence": 0.95,
  "warnings": []
}
```

Обязательные роли:

- `sku_column`
- `name_column`
- `price_column`

Workflow продолжает обработку при `confidence >= 0.8`.

## Нормализованная строка

```json
{
  "source_row_number": 2,
  "sku": "EL-A9F74106",
  "sku_key": "EL-A9F74106",
  "name": "Автоматический выключатель 1P C6 6kA",
  "raw_price": "412,50",
  "price": 412.5,
  "raw_stock": "95",
  "stock": 95,
  "stock_status": "exact",
  "unit": "шт",
  "manufacturer": "Systeme Electric",
  "currency": "RUB",
  "price_status": "ok",
  "duplicate_status": "none",
  "errors": [],
  "warnings": [],
  "is_valid": true,
  "is_exportable": true,
  "has_warnings": false,
  "mapping_confidence": 0.95
}
```

## Статусы дублей

- `none`
- `exact_duplicate_original`
- `exact_duplicate_copy`
- `conflict`

Точная копия исключается, первая строка группы сохраняется с предупреждением. Конфликтующие строки с одним SKU отклоняются целиком.

## Ошибки

- `ROW_INVALID_FORMAT`
- `SKU_EMPTY`
- `NAME_EMPTY`
- `PRICE_EMPTY`
- `PRICE_INVALID_FORMAT`
- `PRICE_NON_POSITIVE`
- `STOCK_NEGATIVE`
- `DUPLICATE_SKU_CONFLICT`

## Предупреждения

- `STOCK_INVALID_FORMAT`
- `STOCK_VALUE_UNKNOWN`
- `STOCK_LOWER_BOUND`
- `UNIT_EMPTY`
- `CURRENCY_UNKNOWN`
- `EXACT_DUPLICATE_GROUP`
- `EXACT_DUPLICATE`
