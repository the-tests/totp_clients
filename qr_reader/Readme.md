# TOTP QR Code reader for Python

## Install

- Install necessary libraries (tested in Ubuntu 24.04)

```shell
# needed for pyzbar
sudo apt install libzbar0
```

- Install dependencies

```shell
pip install opencv-python pyscreenshot numpy pyzbar pillow
```

- Make file executable (optional)

```shell
chmod +x read_qr.py
```

## Run

- Open browser and make QR code visible on screen
- Run `./read_qr.py` to take screenshot and read QR code. You will see output JSON for all QRs:

    ```json
    {
      "name": "Github:yourlogin",
      "digits": 6,
      "interval": 30,
      "secret": "ABCDEF..."
    }
    ```

＊ `digits` and `interval` are hardcoded as most common values for TOTP authenticators and not a part of QR code info
