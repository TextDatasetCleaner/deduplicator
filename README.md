# deduplicator
 Инструмент для выявления нечетких дубликатов строк. Deduplicator представляет из себя web-сервис и может быть использован в процессе работы TDC. Для тестирования предусмотрен пользовательский интерфейс.<br/>
<br/>
На вход подается строка для проверки, deduplicator обрабатывает ее и отправляет ответ:<br/>
TRUE, если строка является нечетким дубликатом для какой-либо из предыдущих введенных строк<br/>
FALSE, если строка уникальна.<br/>

## Установка

Склонировать репозиторий командой:<br/> git clone https://github.com/TextDatasetCleaner/deduplicator
<br/><br/>
Установить зависимости командой:<br/> pip install -r requirements.txt

## Запуск

Запустить командой:<br/> python3 app.py<br/>
<br/>
Открыть в браузере:<br/> http://127.0.0.1:5000
