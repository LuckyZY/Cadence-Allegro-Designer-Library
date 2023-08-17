import os
import shutil
import glob
import time

ALLOWED_EXTENSIONS = ['.dra', '.psm', '.pdf', '.pad', '.step', '.OLB' , '.opj' , '.py']
ALLOWED_FILES = ['.DS_Store']

def clean_files(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file_path)
            if ext not in ALLOWED_EXTENSIONS and filename not in ALLOWED_FILES:
                print(f"删除文件: {file_path}")
                os.remove(file_path)
        elif os.path.isdir(file_path):
            clean_files(file_path)

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    clean_files(path)
    print("程序执行完毕。—— Luck_zy")

if __name__ == "__main__":
    main()