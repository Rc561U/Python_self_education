#!/usr/bin/env python3
from multiprocessing import Pool
import subprocess
import os


def run(task):
    dest = os.getcwd() + '/data/prod_backup/'
    print("Handling {}".format(task))
    subprocess.call(['rsync', '-arq', src, dest])


if __name__ == "__main__":
    src = os.getcwd() + '/data/prod/'
    list = os.listdir(src)
    all_files = []

    for i in list:
        all_files.append(os.path.join(src, i))
    with Pool(len(all_files)) as pool:
        pool.map(run, all_files)
