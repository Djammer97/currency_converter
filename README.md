В приложение встроен uvicorn, т.е. при запуске main.py по localhost:8000 становится возможно делать http-запросы.

Реализованы 4 пути:
1) /auth/register - регистрация пользователя (реализована через простой словарь, т.е. при перезапуске необходимо регистрироваться снова)
2) /auth/login - получение jwt, без которого не будет доступа к путям, связанным с валютами
3) /currency/list - получение списка валют с их кодами, которые необходимы для конвертера (в заголовке Authorization передается jwt)
4) /currency/exchange - конвертет валют. В параметрах запроса нужно указать from_code, to_code, value, а также передать jwt через заголовки
