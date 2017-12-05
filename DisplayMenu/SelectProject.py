import collections
from LoadSetting.LoadSetting import get_deploy_project_by_ip
from Tools.InputComponent import input_multi_item
from Tools.DisplayComponent import create_line_format


def display_project_menu(deploy_server_list):
    all_deploy_list = list()
    for server in deploy_server_list:
        loop_flag = True                                                                # 控制输入错误的循环
        while loop_flag:
            server_info = get_deploy_project_by_ip(server[0], server[1])                # server[0]:IP, server[1]:类型
            print('######################################################################')
            create_line_format('Choose Deploy Project On {}'.format(server[0]), None, 14)
            print('######################################################################')
            create_line_format('0 All Project', None, 25)                               # 发布全部服务的选项
            project_list = server_info['Projects']
            project_dict = collections.OrderedDict()
            project_index_list = list()
            for index in range(len(project_list)):                                      # 循环输出所有Project
                create_line_format(project_list[index]['Name'], index, 25)
                project_index_list.append(str(index + 1))
                project_dict[str(index + 1)] = project_list[index]
            print('######################################################################')
            loop_flag, sequence_list = input_multi_item('Choose your project to deploy [eg: 1 2 ...]:', project_index_list)

            if loop_flag:                                                               # 如果用户调皮了,那就重新输入
                continue
            else:                                                                       # 如果用户没有调皮,将用户所选择的站点/服务的参数整合成字典
                deploy_project_dict = dict()
                deploy_project_list = list()
                for item in sequence_list:
                    deploy_project_list.append(project_dict[item])
                deploy_project_dict['Projects'] = deploy_project_list
                deploy_project_dict['IP'] = server_info['IP']
                deploy_project_dict['UserName'] = server_info['UserName']
                deploy_project_dict['PassWord'] = server_info['PassWord']
                deploy_project_dict['Type'] = server[1]

                all_deploy_list.append(deploy_project_dict)
    print('######################################################################')

    return all_deploy_list

