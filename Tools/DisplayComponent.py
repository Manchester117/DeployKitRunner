def create_line_format(sequence, index, space_num):                     # space_num: 第一个#和第一个实际字符之间有多少个空格
    print("#", end='')
    for i in range(space_num):
        print(' ', end='')
    if index is None:                                                   # 如果想自定义输出位置,index设置为None
        sequence = '{}'.format(sequence)
    else:
        sequence = '{} {}'.format(str(index + 1), sequence)
    print(sequence, end='')
    left_str_num = 70 - space_num - len(sequence) - 2                   # 控制台窗口打印格式(单行)
    for i in range(left_str_num):
        print(' ', end='')
    print('#')
