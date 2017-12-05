import subprocess


def command_execute(cmd):
    process = subprocess.Popen(cmd,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               shell=True,
                               encoding='GBK')
    return process
