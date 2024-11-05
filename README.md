# traffic-usage-log
Logs traffic usage of desired network interfaces in intervals.

## Quick start:

* Instead of `vim` you can use the editor of your choice.
1. Make a copy of `example.env` as `.env`
    ```shell
    cp example.env .env
    ```
2. Edit `.env` and fill required fields
    ```shell
    vim .env
    ```
3. Make a copy of `example_start.sh` as `start.sh`
    ```shell
    cp example_start.sh start.sh
    ```
4. Edit `start.sh` and fill required fields
    ```shell
    vim start.sh
    ```
5. Start server by running `start.sh`
    ```shell
    chmod +x start.sh
    ./start.sh
    ```
