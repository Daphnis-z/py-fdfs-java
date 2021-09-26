import random
import time
import traceback
from uuid import uuid1

from fdfs_java_helper import FdfsJavaHelper


# from fdfs_py_helper import FdfsPyHelper


def test_fastdfs_download():
    # Java
    fdfs_helper = FdfsJavaHelper()

    # Python
    # fdfs_helper = FdfsPyHelper()

    times = 1
    while times <= 100:
        file_num = random.randint(1, 4)
        if file_num == 1:
            ext = '.docx'
            fast_file = 'group1/M00/00/00/wKjTZWFOfDCAK0cAACoRBJY_8Lk80.docx'
        elif file_num == 2:
            ext = '.jpg'
            fast_file = 'group1/M00/00/00/wKjTZWFMgseAElkNAAPCZHy3PIk543.jpg'
        else:
            ext = '.pdf'
            fast_file = 'group1/M00/00/00/wKjTZWFOfEeAC7FPAxpmdPy56gI553.pdf'

        dwn_file = str(uuid1()) + ext
        print('{}. start to download {} ..'.format(times, dwn_file))
        start_time = time.time()
        try:
            fdfs_helper.download_file(fast_file, 'tmp/' + dwn_file)
        except:
            print(traceback.format_exc())
        print('{} is download complete,cost: {} s'.format(dwn_file, round(time.time() - start_time, 3)))

        times = times + 1
        time.sleep(1)


if __name__ == '__main__':
    test_fastdfs_download()
