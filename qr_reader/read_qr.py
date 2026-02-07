#!/usr/bin/env python

import json
import pyscreenshot as ImageGrab
import cv2
import numpy as np

from urllib.parse import parse_qs
from pyzbar.pyzbar import decode

img_pil = ImageGrab.grab()
results = decode(cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR))
for qr in results:
    qr = qr.data.decode("utf-8")
    # otpauth://totp/GitHub:yourname?secret=BLAHBLAHBLAH&issuer=GitHub
    if qr.startswith("otpauth://") and "/totp/" in qr:
        info_line = qr.split("/")[-1].split("?")
        if len(info_line) != 2:
            print(f"Bad QR code info: {qr}")
            continue
        secret = parse_qs(info_line[1])["secret"][0]
        data = {
            "name": info_line[0],
            "digits": 6,
            "interval": 30,
            "secret": secret,
        }
        print(json.dumps(data, indent=2))
