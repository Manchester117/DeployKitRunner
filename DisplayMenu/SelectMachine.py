import collections
from Tools.InputComponent import input_multi_item
from Tools.DisplayComponent import create_line_format


def display_server_menu(deploy_server_param):
    loop_flag = True
    while loop_flag:
        index = 0                                                                                   # 初始化菜单选项索引
        sort_server_dict = collections.OrderedDict()

        print('######################################################################')
        create_line_format('Choose All Server', None, 25)
        print('######################################################################')
        create_line_format('0 All Server', None, 27)                                                # 发布全部机器的选项

        deploy_website_param = deploy_server_param['WebSite']
        print('######################################################################')
        create_line_format('Choose WebSite IP', None, 25)
        print('######################################################################')
        for server in deploy_website_param:
            index = deploy_website_param.index(server)
            create_line_format(server['IP'], index, 25)
            sort_server_dict[str(index + 1)] = (server['IP'], 'WebSite')
        print('######################################################################')

        const_index = index + 1
        deploy_service_param = deploy_server_param['Service']
        print('######################################################################')
        create_line_format('Choose Service IP', None, 25)
        print('######################################################################')
        for server in deploy_service_param:
            index = deploy_service_param.index(server) + const_index
            create_line_format(server['IP'], index, 25)
            sort_server_dict[str(index + 1)] = (server['IP'], 'Service')
        print('######################################################################')

        server_index_list = sort_server_dict.keys()                                                 # 获取每个IP的选项索引

        loop_flag, sequence_list = input_multi_item('Choose your server to deploy [eg: 1 2 ...]: ', server_index_list)
        deploy_server_list = list()
        for item_index in sequence_list:
            deploy_server_list.append(sort_server_dict[item_index])

        return deploy_server_list
