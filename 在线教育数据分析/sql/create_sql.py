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

board2 = {
    'new_customer_remain_day': {'data': 0, 'avg': 0},  # 新用户次留存 {data:数值,avg:30天平均值}
    'new_customer_remain_week': {'data': 0, 'avg': 0},  # 新用户周留
    'active_customer_remain_day': {'data': 0, 'avg': 0},  # 活跃次留
    'active_customer_remain_week': {'data': 0, 'avg': 0},  # 活跃周留
    'product_details': {'data': 0, 'avg': 0},  # 浏览商详人数
    'reservation': {'data': 0, 'avg': 0},  # 预约人数
    'product_details_rate': {'data': 0, 'avg': 0},  # 浏览人数训练营转换率
    'reservation_rate': {'data': 0, 'avg': 0}
}

# sql1= 'avg ({v}) as {v}_avg,'
# for v in board2.keys():
#     print(sql1.format(v=v))

# sql3 = '''current.{v} as {v}_num,
# if( last_2.{v} = 0, last_1.{v}, (last_1.{v} - last_2.{v})/last_2.{v} ) as {v}_rate_day,
# if( last_7.{v} = 0, current.{v}, (current.{v} - last_7.{v})/last_7.{v} ) as {v}_rate_week,
# '''
# for v in board1.keys():
#     print(sql3.format(v=v))

sql2 = '''current.{v} as {v}_data,
f1.{v}_avg as {v}_avg,
'''
for v in board2.keys():
    print(sql2.format(v=v))