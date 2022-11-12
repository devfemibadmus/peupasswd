from .pencryptor import pencryptor

def peupasswd(master_passwd: str, service_name: str, passwd_length: int):
    list = [master_passwd, service_name, passwd_length]
    if len(list) == 3:
      peupasswd = pencryptor(master_passwd, service_name, passwd_length)
    else:
      peupasswd = "master passwd or service name or passwd length missing"
    return peupasswd
