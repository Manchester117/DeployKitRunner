from ActionExec.ActionWrapper import compile_code_run
from Tools.DisplayComponent import create_line_format
from Tools.InputComponent import input_single_item


def display_is_local_compile(compile_code_param):
    loop_flag = True
    while loop_flag:
        menu_list_with_flag = [('Compile Code', True), ('Not Compile Code', False)]
        menu_list = [item[0] for item in menu_list_with_flag]
        print('######################################################################')
        for index in range(len(menu_list)):
            create_line_format(menu_list[index], index, 25)
        print('######################################################################')
        loop_flag, selected_item = input_single_item('Enter your choose item: ', len(menu_list))
        if loop_flag is False:
            item_flag = menu_list_with_flag[selected_item - 1][1]                       # 获取列表中的标志位,用于判断是否本地编译
            compile_code_run(compile_code_param, item_flag)                             # 执行编译
            break


if __name__ == '__main__':
    display_is_local_compile()