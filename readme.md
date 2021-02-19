# 🎧 Statusify

Транслируйте музыку, которая играет у Вас в **Spotify** в **Ваш статус ВКонтакте**

## Установка

Клонируйте репозиторий

```bash
git clone https://github.com/alxxndrv/statusify.git
```

Установите нужные модули из `requirements.txt`
```bash
pip install -r requirements.txt
```

Вам понадобятся некоторые **глобальные переменные**

Для начала, зарегистрируйте свое приложение на [портале для разработчиков Spotify](http://developer.spotify.com)

Вам понадобятся:

1. `Client ID`
2. `Client Secret`

В меню приложения, нажмите __Edit Settings__, и в поле `Redirect URIs` добавьте любой URL. Абсолютно любой.

Добавьте имеющиеся на данный момент данные в глобальные переменные:

__macOS__

Для начала, Client ID:
```bash
export SPOTIPY_CLIENT_ID=YOUR_CLIENT_ID
```
Затем, Client Secret:
```bash
export SPOTIPY_CLIENT_SECRET=YOUR_CLIENT_SECRET
```
И, наконец, Redirect URI. Укажите тот, что вписали в портале разработчиков:
```bash
export SPOTIPY_REDIRECT_URI=example.com/redir
```

Теперь получим `access token` ВКонтакте

Перейдите на сайт [https://vkhost.github.io](https://vkhost.github.io) и выберите ***Kate Mobile***

Дайте разрешения для API, затем скопируйте `access_token` из адресной строки.

Добавьте его в глобальные переменные:

__macOS__

```bash
export VK_TOKEN=YOUR_VK_TOKEN
```
Готово! Переходим к ***запуску.***

## Использование

```bash
python app.py start_phrase stop_phrase
```
...где `start_phrase` —  это фраза, которая должна появится у человека в статусе ВКонтакте, после которой начнется трансляция музыки в статус; `stop_phrase` — фраза, после появление которой в статусе через определенный интервал прекратится трансляция треков.

Например,
```bash
python app.py start stop
```

![статус_вконтакте](https://i.ibb.co/5cqZ7dk/Screenshot-2021-02-20-at-02-08-1.png)

## Поддержка
`Pull requestы` приветствуются. Если хотите сделать большое изменение — откройте `issue`. 

## Лицензия
[Mozilla Public License 2.0](https://choosealicense.com/licenses/mpl-2.0/)
