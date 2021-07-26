data1 = [0, 0, 0, 0, 3, 7, 10, 12, 7, 3, 0, 0, 2, 5, 6, 0, 0, 0]
data2 = [0, 0, 0, 1, 4, 7, 8, 10, 6, 5, 1, 0, 1, 4, 7, 0, 0, 0]
data3 = [0, 0, 0, 2, 6, 9, 10, 12, 7, 4, 2, 0, 2, 5, 6, 1, 0, 0]
data4 = [0, 0, 1, 0, 1, 6, 11, 11, 0, 4, 1, 1, 4, 8, 2, 2, 0, 0]
data5 = [0, 0, 0, 0, 1, 6, 11, 11, 0, 4, 1, 1, 4, 8, 2, 0, 0, 0]

data_lst = [data1, data2, data3, data4, data5]
rounding = 3


def each_data_printer(complete_data_list):
    for i, data in enumerate(complete_data_list):
        print(f"data {i}: {data}")


def average_lst_calculator(complete_data_list):
    ava_divider = len(complete_data_list)
    calc = 0
    ava_data = []
    each_data_printer(complete_data_list)
    for r in range(len(complete_data_list[0])):
        for i, data in enumerate(complete_data_list):
            calc += complete_data_list[i][r]
        if calc == 0:
            calc = calc
        else:
            calc = calc / ava_divider
            calc = round(calc, rounding)
        ava_data.append(calc)
    print(f"average: {ava_data}")


if __name__ == '__main__':    
    average_lst_calculator(data_lst)
