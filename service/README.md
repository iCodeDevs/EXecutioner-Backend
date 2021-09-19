# Service setup

## Installation

- copy rqworker.service to /etc/systemd/system folder (requires sudo)

- start systemd unit

    ```bash
    sudo systemctl start rqworker.service
    ```

- check status

    ```bash
    sudo systemctl status rqworker.service
    ```

## Notes

- User - change user to the user that installed all dependencies

- WorkingDirectory

  - folder should belong to the user of service

  - should be absolute path to the repository

- ExecStart

  - should be absolute path to repository/service/start_service.sh

- EnvironmentFile

  - should be absolute path to repository/.env
  - contains REDIS_URL value
