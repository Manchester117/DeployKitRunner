def input_single_item(input_title, menu_length):
    selected_item = input(input_title)

    if selected_item.isdigit():                 # 先判断输入是不是数字
        for item in range(1, menu_length + 1):  # 再判断输入在不在菜单选项范围内(菜单长度需要+1)
            if selected_item == str(item):
                return False, item
        else:
            print("菜单中没有所输入的选项...")
            input('Press any key to continue...')
            return True, 0
    else:
        print("同学...你又调皮了..重新来过吧...")
        input('Press any key to continue...')
        return True, 0


def input_multi_item(input_title, all_menu_item):
    sequence_item = input(input_title)
    sequence_list = sequence_item.strip().split(' ')

    for item in sequence_list:                                                  # 先判断输入的每一项是不是数字
        if item.isdigit() is False:
            print("同学...你又调皮了..重新来过吧...")
            input('Press any key to continue...')
            return True, list()
    sequence_list = sorted(set(sequence_list), key=sequence_list.index)         # 列表去重,并保证顺序

    if '0' in sequence_list:
        return False, list(all_menu_item)                                       # 如果输入中包含0,则代表全选

    for item in sequence_list:                                                  # 再判断输入的列表中是否有不存在的编号
        if item not in all_menu_item:
            print("不存在输入的服务器,请对比所输入的服务器编号和菜单中所给的服务器编号...")
            input('Press any key to continue...')
            return True, list()
    return False, sequence_list



