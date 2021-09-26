# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: Daphnis
# Github: https://github.com/Daphnis-z
# CreatDate: 2021/9/26 20:29
# Description: 使用原生 Python下载 fastdfs文件

from fdfs_client.client import get_tracker_conf, Fdfs_client


class FdfsPyHelper:

    def __init__(self, fdfs_config='etc/fastdfs.properties'):
        tracker_conf = get_tracker_conf(fdfs_config)
        self.fdfs_client = Fdfs_client(tracker_conf)

    def download_file(self, file_path, local_file=None):
        if local_file is None:
            target_file = 'download' + file_path[file_path.rfind('/'):]
        else:
            target_file = local_file
        self.fdfs_client.download_to_file(target_file, file_path.encode())

        return target_file
