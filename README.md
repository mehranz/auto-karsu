# Auto Karsu

a small utility to automatically submit employees working start and end time to karsu system.

### how to use
#### install dependencies:
you can install dependencies simply by run:
```shell
$ pip install -r requirements.txt
```

__** probably you prefer to create a venv and install dependencies inside it.__


#### put tokens inside config
open src/config.py file and fill and fill `EMAILS_TOKENS` variable as described.

this approach is wrong anyway and should be changed to something editable on runtime (such as a db) soon.

#### run the script
executing the main file will run the script. though it can be a good idea to create a systemd unit.

```shell
$ python main.py
```