# Обрезка ссылок с помощью Битлинк
HTTP сервис для сокращения URL наподобие Bitly и других сервисов.

Есть возможность:

* сохранить короткое представление заданного URL
* перейти по сохраненному ранее короткому представлению и получить redirect на соответствующий исходный URL
* валидация URL с проверкой корректности ссылки

Программа запрашивает ссылку, делает битлинк, если ссылка им не является, иначе выводит количество кликов по ней

```
python main.py https://docs.python.org/3.6/howto/argparse.html
Битлинк https://bit.ly/3BbJKFh
```
```
python main.py https://bit.ly/3BbJKFh
0
```

## Как установить
1. Создайте переменную окружения API_BITLINK_TOKEN и положите в неё токен API Bitly. 
Зарегистрируйтесь [здесь](https://app.bitly.com/Bm6mipUaka0/bitlinks/3BbJKFh)

2. Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.