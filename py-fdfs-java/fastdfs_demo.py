import random
import time
import traceback
from uuid import uuid1

from fdfs_client.client import get_tracker_conf, Fdfs_client


def main():
    tracker_conf = get_tracker_conf('etc/fastdfs.properties')
    client = Fdfs_client(tracker_conf)

    # 列出所有的group信息
    # result = client.list_all_groups()
    # print(result)

    # 文件上传，结果返回：{'Group name': b'group1', 'Remote file_id': b'group1/M00/00/00/wKgf3F5MAe2AV_23AAAADL_GVeU370.txt', 'Status': 'Upload successed.', 'Local file name': 'test.txt', 'Uploaded size': '12B', 'Storage IP': b'192.168.31.220'}
    # result = client.upload_by_filename(r'test\demo-data\宁夏生态保护与建设“十三五”规划.txt')
    # print(result['Local file name'], ',', result['Remote file_id'])

    # 文件下载，结果返回：{'Remote file_id': b'group1/M00/00/00/wKgf3F5MAe2AV_23AAAADL_GVeU370.txt', 'Content': 't.txt', 'Download size': '12B', 'Storage IP': b'192.168.31.220'}
    file_path = 'group1/M00/00/00/wKjTZWFMgseAElkNAAPCZHy3PIk543.jpg'
    file_bytes = bytes(file_path, 'utf-8')
    result = client.download_to_file('gsl.jpg', file_bytes)
    print(result)

    # print(str(uuid1()).replace('-', ''))

    # # 文件删除，结果返回：('Delete file successed.', b'group1/M00/00/00/wKgf3F5MAe2AV_23AAAADL_GVeU370.txt', b'192.168.31.220')
    # result = client.delete_file(b'group1/M00/00/00/wKgf3F5MAe2AV_23AAAADL_GVeU370.txt')

    # 列出同一组内的storage servers信息
    # result = client.list_servers(b'group1')
    # print(result)


def test_fastdfs():
    tracker_conf = get_tracker_conf('config/fastdfs.properties')
    client = Fdfs_client(tracker_conf)

    times = 1
    while times <= 2:
        start_time = time.time()

        file_num = random.randint(1, 4)
        if file_num == 1:
            ext = '.docx'
            fast_file = b'group1/M00/0C/9B/CoNuFV8Nb-2AdUEBAAA0UAJnrTs59.docx'
        elif file_num == 2:
            ext = '.txt'
            fast_file = b'group1/M00/0C/9B/CoNuFV8NcCmAWXlJAAAIAM02UYw328.txt'
        else:
            ext = '.pdf'
            fast_file = b'group1/M00/0C/9B/CoNuFV8NcEmAODEjAAPekBVkJBc708.pdf'

        dwn_file = str(uuid1()) + ext

        print('{}. start to download {} ..'.format(times, dwn_file))
        try:
            client.download_to_file('fdfs/' + dwn_file, fast_file)
        except:
            print(traceback.format_exc())
        print('{} is download complete,cost: {} s'.format(dwn_file, round(time.time() - start_time, 3)))

        times = times + 1
        time.sleep(1)


if __name__ == '__main__':
    main()
    # test_fastdfs()
