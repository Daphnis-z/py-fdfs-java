# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: Daphnis
# Github: https://github.com/Daphnis-z
# CreatDate: 2021/9/25 9:46
# Description:
import os

import jpype

# 在 Linux上推荐直接指定 libjvm.so的位置，不要用 getDefaultJVMPath()
JVM_SO_PATH = jpype.getDefaultJVMPath()
JAR_PATH = 'lib/fastdfs-client-java-1.28.jar'


class FdfsJavaHelper:
    def __init__(self, fdfs_config='etc/fastdfs.properties'):
        jpype.startJVM(JVM_SO_PATH, '-ea', '-Djava.class.path={}'.format(JAR_PATH))
        self.fdfs_client = jpype.JClass('com.daphnis.fdfs.FdfsClient')
        self.fdfs_client.init(fdfs_config)

    def download_file(self, file_path, local_file=None):
        group = file_path[0:file_path.find('/')]
        dfs_path = file_path[file_path.find('/') + 1:]
        if local_file is None:
            target_file = 'download' + file_path[file_path.rfind('/'):]
        else:
            target_file = local_file
        self.fdfs_client.downloadFile(group, dfs_path, target_file)

        # 检查下载结果
        if not os.path.exists(target_file):
            raise IOError('[-] Error: use java download fastdfs file fail !!')

        return target_file
