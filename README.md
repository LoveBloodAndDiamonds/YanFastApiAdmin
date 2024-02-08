# YanSQLAdminAPI
API сервис на sqladmin содержащий в себе веб-интерфейс для управления базой данных.


## Инструация по установке и запуску
Инструкция написана для linux ubuntu 22.04, на других дистрибутивах команды могут отличаться.

1. Обновите список версий пакетов:
   ```shell
   sudo apt update
2. Обновите пакеты:
   ```shell
   sudo apt upgrade
3. Скопируйте репозиторий:
   ```shell
   git clone https://github.com/LoveBloodAndDiamonds/YanSQLAdminAPI.git
4. Заполните .env.example и переименуйте его в .env
   ```shell
   nano env.example
   ```
5. Запустите следующую команду в терминале на вашем сервере:
   ```shell
   curl -fsSL https://get.docker.com -o get-docker.sh
6. Затем запустите скрипт установки Docker:
   ```shell
   sudo sh get-docker.sh
7. После завершения установки Docker, добавьте текущего пользователя в группу docker, чтобы иметь возможность запускать Docker без использования sudo:
   ```shell
   sudo usermod -aG docker $USER
8. Установите Docker Compose:
   ```shell
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
9. Измените разрешения для Docker Compose:
   ```shell
   sudo chmod +x /usr/local/bin/docker-compose
10. Запустите контейнер:
   ```shell
   docker-compose up -d
