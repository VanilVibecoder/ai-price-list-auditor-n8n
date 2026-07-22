# Security Policy

## Поддерживаемая версия

Репозиторий содержит демонстрационную версию workflow.

## Секреты

Никогда не коммитьте:

- Telegram bot token;
- credential JSON;
- `.env`;
- реальные клиентские прайсы;
- экспорт execution data;
- pinned data из production;
- внутренние webhook и instance identifiers.

Публичный workflow очищен от credential references, webhook ID, instance metadata и pin data.

## Данные

Для публичных тестов используйте только синтетические данные из `samples/`.

## Сообщение об уязвимости

Не публикуйте секреты в issue. Отзовите скомпрометированный токен и замените credential в n8n.
