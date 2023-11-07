# Pyton TOTP client for command line

## Install

- Install dependencies

```shell
sudo pip install pyotp
sudo chown root:root totp
sudo chmod +x totp
```

- Copy executable

```
sudo mv totp /usr/bin/totp
```

- By default python interpreter path set as: `/usr/bin/python3`. It should be edited if your python path is different (see first line of `totp` file)

## Configure

- Open configuration file in text editor

```
nano ~/.config/.keys.json
```

- Add records

```
[
  {
    "name": "github",
    "digits": 6,
    "interval": 30,
    "secret": "23456ABCDEFGHJIK"
  },
  {
    "name": "microsoft",
    "digits": 6,
    "interval": 30,
    "secret": "ABCDEFGHJIK23456"
  }
]
```

## Run

- Start

```shell
$ totp

   github 860217 |=====================_________|
   microsoft 783733 |=====================_________|


```

- `Ctrl+C` to Stop
