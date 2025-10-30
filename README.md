# Парсер статей с Habr.com

Python-скрипт для сбора данных о популярных статьях с сайта Habr.com.

## Установка

### 1. Клонирование репозитория

```bash
git clone https://github.com/your-username/parser_habr.git
cd parser_habr
```

### 2. Установка зависимостей

```bash
poetry install
```

**Необходимые пакеты:**
- `aiohttp` - для выполнения HTTP-запросов
- `beautifulsoup4` - для парсинга HTML
- `lxml` - парсер для BeautifulSoup
- `fake-useragent` - для генерации случайных User-Agent

Файл `requirements.txt` должен содержать:
```
aiohappyeyeballs==2.6.1
aiohttp==3.13.1
aiosignal==1.4.0
attrs==25.4.0
beautifulsoup4==4.14.2
frozenlist==1.8.0
idna==3.11
lxml==6.0.2
multidict==6.7.0
propcache==0.4.1
soupsieve==2.8
typing_extensions==4.15.0
yarl==1.22.0
```

## Запуск

```bash
python main.py
```