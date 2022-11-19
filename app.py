# System requirements (need to install as dependencies):
# 1. poppler (for pdf2image, convert pdf to images list)
# 2. zbar (for pyzbar, finding anf reading qr codes on images)

# OS X zbar resolve fix:
# mkdir ~/lib
# ln -s $(brew --prefix zbar)/lib/libzbar.dylib ~/lib/libzbar.dylib

import json
import os
import sys
from pathlib import Path
from typing import Dict, List

from pdf2image import convert_from_path
from pyzbar.pyzbar import Decoded, ZBarSymbol, decode


def bank_account_parser(data:str) ->Dict[str,str]:
    """Parse '|' separate key,value data from qr code decoded string"""

    fields = data.split('|')[1:]
    result = {}
    for f in fields:
        k,v = f.split('=', 1)
        result[k] = v
    return result


def process_pdf_file(filename:str) -> List[Dict[str,str]]:
    images = convert_from_path(filename)
    result = []
    for img in images:
        founded:List[Decoded] = decode(img, symbols=[ZBarSymbol.QRCODE])
        for qr in founded:
            data = qr.data.decode('utf-8')
            result.append(bank_account_parser(data))
    return result


if len(sys.argv)>=2:
    filename = sys.argv[1]
    result = process_pdf_file(filename)
    output = open(f'{filename.rsplit(".",1)[0]}.json', 'w')
    json.dump(result, output, ensure_ascii=False, indent=4)
else:
    print('pdf file required as first arg')
