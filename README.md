# Usage

`python3 app.py sample.pdf`

Resulting JSON file should appear near provided pdf file.

# System dependecies (examples for OS X, same for linux packet managers):

1. `brew install poppler` (for pdf2image, convert pdf to images list)
2. `brew install zbar` (for pyzbar, finding anf reading qr codes on images)


# OS X zbar lib mapping for pyzbar:
```
mkdir ~/lib

ln -s $(brew --prefix zbar)/lib/libzbar.dylib ~/lib/libzbar.dylib
```

# Python3 dependecies

1. `pip3 install pdf2image`
2. `pip3 install pyzbar`

