import time

from fdfs_client.client import get_tracker_conf, Fdfs_client


class FastdfsHelper:

    def __init__(self, fastdfs_config):
        tracker_conf = get_tracker_conf(fastdfs_config)
        self.fastdfs_client = Fdfs_client(tracker_conf)

    def download_file(self, file_path, local_file=None):
        start_time = time.time()
        print('start to download file: ' + file_path)

        if local_file is None:
            target_file = 'download' + file_path[file_path.rfind('/'):]
        else:
            target_file = local_file
        result = self.fastdfs_client.download_to_file(target_file, file_path.encode())
        print('start to download file: ' + file_path)

        print('fastdfs file is save to {},cost {}s'.format(target_file, round(time.time() - start_time, 3)))
        return target_file, result['Download size']
