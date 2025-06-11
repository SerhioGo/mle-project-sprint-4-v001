# Подготовка виртуальной машины

## Склонируйте репозиторий

Склонируйте репозиторий проекта:

```
git clone https://github.com/yandex-praktikum/mle-project-sprint-4-v001.git
```

## Активируйте виртуальное окружение

Используйте то же самое виртуальное окружение, что и созданное для работы с уроками. Если его не существует, то его следует создать.

Создать новое виртуальное окружение можно командой:

```
python3 -m venv env_recsys_start
```

После его инициализации следующей командой

```
. env_recsys_start/bin/activate
```

установите в него необходимые Python-пакеты следующей командой

```
pip install -r requirements.txt
```

### Скачайте файлы с данными

Для начала работы понадобится три файла с данными:
- [tracks.parquet](https://storage.yandexcloud.net/mle-data/ym/tracks.parquet)
- [catalog_names.parquet](https://storage.yandexcloud.net/mle-data/ym/catalog_names.parquet)
- [interactions.parquet](https://storage.yandexcloud.net/mle-data/ym/interactions.parquet)
 
Скачайте их в директорию локального репозитория. Для удобства вы можете воспользоваться командой wget:

```
wget https://storage.yandexcloud.net/mle-data/ym/tracks.parquet

wget https://storage.yandexcloud.net/mle-data/ym/catalog_names.parquet

wget https://storage.yandexcloud.net/mle-data/ym/interactions.parquet
```

## Запустите Jupyter Lab

Запустите Jupyter Lab в командной строке

```
jupyter lab --ip=0.0.0.0 --no-browser
```

# Расчёт рекомендаций

Код для выполнения первой части проекта находится в файле `recommendations.ipynb`. Изначально, это шаблон. Используйте его для выполнения первой части проекта.

# Сервис рекомендаций

Код сервиса рекомендаций находится в файле `recommendations_service.py`.
Код класса рекоммендаций для основного сервиса находится в файле `cl_recommendations.py`. Код сервиса для получения похожих обьектов для item_id находится В файле под названием `features_service.py` - код для получения схожих объектов. Соотвественно, код сервиса для сохранения/получения истории действий пользователя находится в файле `events_service.py`. Для корректной работы, необходимо запустить каждую сервис в разных терминалах поочередно.

Ниже прдетсавлен код для выполнения в терминале №1:

cd mle-project-sprint-4-v001/
source env_recsys_start/bin/activate
uvicorn recommendation_service:app

Ниже прдетсавлен код для выполнения в терминале №2:

cd mle-project-sprint-4-v001/
source env_recsys_start/bin/activate
uvicorn features_service:app --port 8010

Ниже прдетсавлен код для выполнения в терминале №3:

cd mle-project-sprint-4-v001/
source env_recsys_start/bin/activate
uvicorn events_service:app --port 8020

# Инструкции для тестирования сервиса

Код для тестирования сервиса находится в файле `test_service.py`.
Результат теста сохраняется в файл `test_service.log`.

Ниже прдетсавлен код для выполнения тестового сервиса:
cd mle-project-sprint-4-v001/
source env_recsys_start/bin/activate
python test_service.py
