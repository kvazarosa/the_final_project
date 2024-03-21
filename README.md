﻿ Авто-Тест на создание заказа и получение заказа по треку с помощью API Яндекс Самокат.
Для запуска тестов должны быть установлены пакеты pytest и requests
Запуск всех тестов выполняется командой pytest

 Условие задачи для автоматизации теста к API
1. Клиент создает заказ
2. Проверяется, что по треку заказа можно получить данные о заказе.

 Шаги автотеста:
1. Выполнить запрос на создание заказа.
2. Сохранить номер трека заказа.
3. Выполнить запрос на получения заказа по треку заказа.
4. Проверить, что код ответа равен 200.
