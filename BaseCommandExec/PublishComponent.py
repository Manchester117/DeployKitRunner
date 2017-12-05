import time
import wmi
from BaseCommandExec.CommandExecute import command_execute


def pull_code_task(pull_code_param):
    cmd = [
        pull_code_param['TFPath'],
        'get',
        pull_code_param['SolutionPath'],
        pull_code_param['WorkSpace'],
        '/login:{},{}'.format(pull_code_param['UserName'], pull_code_param['PassWord'])
    ]
    process = command_execute(cmd)
    for line in process.stdout:
        print(line, end='')


def compile_task(compile_sln_param):
    cmd = [
        compile_sln_param['MSBuildPath'],
        '{}\\{}\\{}.sln'.format(compile_sln_param['WorkSpace'], compile_sln_param['SolutionName'], compile_sln_param['SolutionName']),
        '/t:Rebuild',
        '/p:Configuration=Debug',
        '/p:VisualStudioVersion=14.0'
    ]
    process = command_execute(cmd)
    for line in process.stdout:
        print(line, end='')


def deploy_task(deploy_param):
    """
    :description: 复制文件之前增加一层,方便后续扩展
    :param deploy_param:
    :return:
    """
    copy_compile_file(deploy_param['Projects'])


def copy_compile_file(server_deploy_list):
    for deploy_info in server_deploy_list:
        cmd = [
            'robocopy',
            deploy_info['Sources'],
            deploy_info['Destination'],
            '/e'
        ]
        # 过滤忽略文件夹
        ignore_folders = deploy_info['IgnoreFile']['Folder']
        if ignore_folders is not None:
            filter_folder_cmd = ['/xd']
            filter_folder_cmd.extend(ignore_folders)
            cmd.extend(filter_folder_cmd)

        # 过滤掉忽略文件,对pdb文件进行单独处理
        ignore_files = deploy_info['IgnoreFile']['File']
        if ignore_files is not None:
            ignore_files[ignore_files.index('.pdb')] = '*.pdb'
            filter_file_cmd = ['/xf']
            filter_file_cmd.extend(ignore_files)
            cmd.extend(ignore_files)

        # 执行命令
        process = command_execute(cmd)
        for line in process.stdout:
            print(line, end='')


def connect_server(server_info):
    cmd = [
        'net',
        'use',
        '\\\\{}\ipc$'.format(server_info['IP']),
        server_info['PassWord'],
        '/user:{}'.format(server_info['UserName']),
    ]
    process = command_execute(cmd)
    for line in process.stdout:
        print(line, end='')


def disconnect_server(server_info):
    cmd = [
        'net',
        'use',
        '\\\\{}'.format(server_info['IP']),
        '/delete',
        '/y'
    ]
    process = command_execute(cmd)
    for line in process.stdout:
        print(line, end='')


def uninstall_service(server_info):
    for project in server_info['Projects']:
        stop_service(server_info['IP'], project['Name'])
        print('停止服务')
        exec_remote_bat(server_info['IP'], server_info['UserName'], server_info['PassWord'], '!UnInstallApp')
        print('卸载服务')
        kill_service_process(server_info['IP'], 'ZhaoPin.HighEnd.TaskSystem.WinService.exe')
        print('杀掉进程')


def install_service(server_info):
    for project in server_info['Projects']:
        exec_remote_bat(server_info['IP'], server_info['UserName'], server_info['PassWord'], '!installApp')
        print('安装服务,暂停5秒,等待服务被系统注册')
        time.sleep(5)
        start_service(server_info['IP'], project['Name'])
        print('启动服务')


def start_service(ip, service_name):
    cmd = [
        'sc',
        '\\\\{}'.format(ip),
        'start',
        service_name
    ]
    process = command_execute(cmd)
    for line in process.stdout:
        print(line, end='')


def stop_service(ip, service_name):
    cmd = [
        'sc',
        '\\\\{}'.format(ip),
        'stop',
        service_name
    ]
    process = command_execute(cmd)
    for line in process.stdout:
        print(line, end='')


def exec_remote_bat(ip_address, username, password, bat_exec):
    try:
        conn = wmi.WMI(computer=ip_address, user=username, password=password)
        file_name = 'C:\wwwroot\HighEndWinService\{}'.format(bat_exec)
        cmd_exec_bat = 'cmd /c call %s' % file_name
        conn.Win32_Process.Create(CommandLine=cmd_exec_bat)
        return True
    except Exception as e:
        print(e)
        return False


def kill_service_process(ip, process_exec):
    cmd = [
        'taskkill',
        '/S',
        ip,
        '/U',
        'administrator',
        '/P',
        'zhuopin',
        '/IM',
        process_exec
    ]
    process = command_execute(cmd)
    for line in process.stdout:
        print(line, end='')

