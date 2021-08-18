b1 = '''    board1['{v}']['num'] = data['{v}_num']
    board1['{v}']['rate_day'] = data['{v}_rate_day']
    board1['{v}']['rate_week'] = data['{v}_rate_week']
    '''

# 面板1
board1 = {
    'total_paying': {'num': 0, 'rate_day': 0, 'rate_week': 0, },  # 总付费人数 {num:人数,rate_day:环比,rate_week:周环比}
    'training_camp': {'num': 0, 'rate_day': 0, 'rate_week': 0, },  # 付费人数训练营
    'special_column': {'num': 0, 'rate_day': 0, 'rate_week': 0, },  # 付费人数专栏
    'vip_member': {'num': 0, 'rate_day': 0, 'rate_week': 0, },  # 付费人数会员
    'activate_user': {'num': 0, 'rate_day': 0, 'rate_week': 0, },  # 激活用户
    'dau': {'num': 0, 'rate_day': 0, 'rate_week': 0, },  # DAU
    'customer_price': {'num': 0, 'rate_day': 0, 'rate_week': 0, },  # 客单价
    'amount': {'num': 0, 'rate_day': 0, 'rate_week': 0, },  # 成交金额
}
# 面板2
board2 = {
    'new_customer_remain_day': {'data': 0, 'avg': 0},  # 新用户次留存 {data:数值,avg:30天平均值}
    'new_customer_remain_week': {'data': 0, 'avg': 0},  # 新用户周留
    'active_customer_remain_day': {'data': 0, 'avg': 0},  # 活跃次留
    'active_customer_remain_week': {'data': 0, 'avg': 0},  # 活跃周留
    'product_details': {'data': 0, 'avg': 0},  # 浏览商详人数
    'reservation': {'data': 0, 'avg': 0},  # 预约人数
    'product_details_rate': {'data': 0, 'avg': 0},  # 浏览人数训练营转换率
    'reservation_rate': {'data': 0, 'avg': 0},  # 预约人数转换率
}

# for v in board1.keys():
#     print(b1.format(v=v))

b2 = '''
board2['{v}']['data'] = data['{v}_data']
board2['{v}']['avg'] = data['{v}_avg']
    '''
for v in board2.keys():
    print(b2.format(v=v))
