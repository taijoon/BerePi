
### 정리가 잘되어 있는 Excel 파일 처리 SW
  - https://github.com/jeonghoonkang/keti/tree/master/BootCamp/cschai/openpyxl

### Install packages
  - excxel packages

### In case of below error
  - UnicodeDecodeError: 'ascii' codec can't decode byte 0xec in position 6: ordinal not in range(128)

### include utf-8 encoding
  - There is many things to do, not the one thing is solution for all error
    - vim /usr/lib/python2.7/sitecustomize.py
      - import sys
      - sys.setdefaultencoding("utf-8")
    - or just add in the __main__

### excel file handling
  - extract, compare, search
  - edit special cells and boxes
