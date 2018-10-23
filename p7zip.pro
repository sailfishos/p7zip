TEMPLATE = subdirs
SUBDIRS = 7z_ \
          7za \
          7zr \
          Format7zFree \
          # rar \ // Disabled for now
          Lzham

BASE_DIR = src/CPP/7zip/QMAKE/
7z_.subdir = $$BASE_DIR/7z_
7z_.target = sub-7z_
7zr.subdir = $$BASE_DIR/7zr
7za.subdir = $$BASE_DIR/7za
Format7zFree.subdir = $$BASE_DIR/Format7zFree
Format7zFree.target = sub-Format7zFree
Lzham.subdir = $$BASE_DIR/Lzham
Lzham.target = sub-Lzham

7z_.depends = sub-Format7zFree sub-Lzham

