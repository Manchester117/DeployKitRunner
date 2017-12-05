import yaml


def get_config_element(config_element):
    yml_file = open('Setting.yaml')
    yml_param = yaml.load(yml_file)
    if config_element == 'PullCodeTask':
        return yml_param['Configuration']['PullCodeTask']
    if config_element == 'CompileTask':
        return yml_param['Configuration']['CompileTask']
    if config_element == 'DeployTask':
        return yml_param['Configuration']['DeployTask']


def get_deploy_task_by_type(deploy_type):
    deploy_task_dict = get_config_element('DeployTask')
    return deploy_task_dict[deploy_type]


def get_deploy_project_by_ip(server_ip, deploy_type):
    server_list_by_type = get_deploy_task_by_type(deploy_type)
    for server_info in server_list_by_type:
        if server_info['IP'] == server_ip:
            return server_info
    else:
        print('Not found Machine...')
        return None


if __name__ == '__main__':
    print(get_config_element('DeployTask'))