from ActionExec.ActionWrapper import pull_code_run
from Tools.DisplayComponent import create_line_format
from Tools.InputComponent import input_single_item


def display_is_pull_code(pull_code_param):
    loop_flag = True
    while loop_flag:
        menu_list_with_flag = [('Pull Code', True), ('Not Pull Code', False)]                   # 定义一个列表,元素中带有标志位
        menu_list = [item[0] for item in menu_list_with_flag]                                   # 从列表中取出菜单项字符串,用于生成菜单
        print('######################################################################')
        for index in range(len(menu_list)):
            create_line_format(menu_list[index], index, 25)
        print('######################################################################')
        loop_flag, selected_item = input_single_item('Enter your choose item: ', len(menu_list))
        if loop_flag is False:
            item_flag = menu_list_with_flag[selected_item - 1][1]                               # 获取列表中的标志位,用于判断是否拉取代码
            pull_code_run(pull_code_param, item_flag)                                           # 执行拉取代码
            break


if __name__ == '__main__':
    display_is_pull_code()