# System requirements (need to install as dependencies):
# 1. poppler (for pdf2image, convert pdf to images list)
# 2. zbar (for pyzbar, finding anf reading qr codes on images)

# OS X zbar resolve fix:
# mkdir ~/lib
# ln -s $(brew --prefix zbar)/lib/libzbar.dylib ~/lib/libzbar.dylib

import os
from pathlib import Path
from typing import Dict, List

from pdf2image import convert_from_path
from pyzbar.pyzbar import Decoded, ZBarSymbol, decode


def bank_account_parser(data:str) ->Dict[str,str]:
    fields = data.split('|')[1:]
    result = {}
    for f in fields:
        k,v = f.split('=', 1)
        result[k] = v
    return result

SAMPLE_FILE = os.path.join(Path(__file__).parent, 'sample.pdf')

images = convert_from_path(SAMPLE_FILE)
for img in images:
    founded:List[Decoded] = decode(img, symbols=[ZBarSymbol.QRCODE])
    for qr in founded:
        data = qr.data.decode('utf-8')
        print(bank_account_parser(data))

