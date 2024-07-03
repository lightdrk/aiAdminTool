import paramiko

class Ssh:
    def __init__(self,creds :dict):
        ''' initialization of Ssh '''
        self.key = creds["key"] or None
        self.sftp = None
        self.port = creds["port"]
        self.user = creds["username"]
        self.hostname = creds["hostname"]
        self.password = creds["password"]
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.private_key = paramiko.RSAKey.from_private_key_file(self.key)

    def connect(self):
        ''' Connect to Server '''
        self.client.connect(self.hostname, self.user, self.password)

    def run(self,command :str):
        ''' run command '''

        stdin, stdout, stderr = self.client.exec_command(command)
        return {stdin, stdout, stderr}

    def sftpConnect(self):
        ''' opening sftp connection ''' 

        self.sftp = self.client.open_sftp()


    def fileUpload(self, upload_from: str, upload_to: str):
        ''' file upload '''
        self.sftp.put(upload_from, upload_to)


    def fileDownload(self, download_from: str, download_to: str):
        ''' download file '''
        self.sftp.get(download_from, download_to)

    def close(self):
        ''' close connection '''
        self.client.close()

    def sftpClose(self):
        ''' close sftp connection '''
        self.client.close()
