# pymvc

Simple Python MVC example.

Available views:
 - `TerminalView`: use stdin/stdout
 - `GUIView`: use [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI) 

Available models:
 - `BasicModel`: store data in dict
 - `RedisModel`: store data in Redis database

## Run

```
virtualenv venv --python=python3
source venv/bin/activate
python main.py
```

## Install optional modules

For `GUIView`:
```
python -m pip install PySimpleGUI
```

For `RedisModel`:
```
python -m pip install redis
```

## Use RedisModel

To use `RedisModel` you also need to have Redis server installed.
E.g. in Ubuntu:
```
sudo apt install redis-server
```
Then, to start local Redis server:
```
redis-server --daemonize yes
```
