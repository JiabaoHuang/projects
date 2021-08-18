import os
import json
import datetime
import pandas as pd
import pymysql
from sqlalchemy import create_engine

# con1 = pymysql.Connection(host='localhost',port='3306',user='root',password='12345678',database='data_job',charset='utf8')
engine = create_engine('mysql+pymysql://root:QaQ111.0@localhost:3306/Level_7_model_1?charset=utf8')
# 读sql
sql = {}

with open(os.path.join('appApi','interface','sql', 'daily_board.sql'), 'r') as f:
    sql['daily_board'] = f.read()

with open(os.path.join('appApi','interface','sql', 'daily_chart.sql'), 'r') as f:
    sql['daily_chart'] = f.read()

with open(os.path.join('appApi','interface','sql', 'weekly_board.sql'), 'r') as f:
    sql['weekly_board'] = f.read()

with open(os.path.join('appApi','interface','sql', 'weekly_chart.sql'), 'r') as f:
    sql['weekly_chart'] = f.read()

weekday_transfer = {
    0: '星期一',
    1: '星期二',
    2: '星期三',
    3: '星期四',
    4: '星期五',
    5: '星期六',
    6: '星期日',
}


def get_board(df_board):
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

    data = json.loads(df_board.loc[0].to_json())
    board1['total_paying']['num'] = data['total_paying_num']
    board1['total_paying']['rate_day'] = data['total_paying_rate_day']
    board1['total_paying']['rate_week'] = data['total_paying_rate_week']

    board1['training_camp']['num'] = data['training_camp_num']
    board1['training_camp']['rate_day'] = data['training_camp_rate_day']
    board1['training_camp']['rate_week'] = data['training_camp_rate_week']

    board1['special_column']['num'] = data['special_column_num']
    board1['special_column']['rate_day'] = data['special_column_rate_day']
    board1['special_column']['rate_week'] = data['special_column_rate_week']

    board1['vip_member']['num'] = data['vip_member_num']
    board1['vip_member']['rate_day'] = data['vip_member_rate_day']
    board1['vip_member']['rate_week'] = data['vip_member_rate_week']

    board1['activate_user']['num'] = data['activate_user_num']
    board1['activate_user']['rate_day'] = data['activate_user_rate_day']
    board1['activate_user']['rate_week'] = data['activate_user_rate_week']

    board1['dau']['num'] = data['dau_num']
    board1['dau']['rate_day'] = data['dau_rate_day']
    board1['dau']['rate_week'] = data['dau_rate_week']

    board1['customer_price']['num'] = data['customer_price_num']
    board1['customer_price']['rate_day'] = data['customer_price_rate_day']
    board1['customer_price']['rate_week'] = data['customer_price_rate_week']

    board1['amount']['num'] = data['amount_num']
    board1['amount']['rate_day'] = data['amount_rate_day']
    board1['amount']['rate_week'] = data['amount_rate_week']

    board2['new_customer_remain_day']['data'] = data['new_customer_remain_day_data']
    board2['new_customer_remain_day']['avg'] = data['new_customer_remain_day_avg']

    board2['new_customer_remain_week']['data'] = data['new_customer_remain_week_data']
    board2['new_customer_remain_week']['avg'] = data['new_customer_remain_week_avg']

    board2['active_customer_remain_day']['data'] = data['active_customer_remain_day_data']
    board2['active_customer_remain_day']['avg'] = data['active_customer_remain_day_avg']

    board2['active_customer_remain_week']['data'] = data['active_customer_remain_week_data']
    board2['active_customer_remain_week']['avg'] = data['active_customer_remain_week_avg']

    board2['product_details']['data'] = data['product_details_data']
    board2['product_details']['avg'] = data['product_details_avg']

    board2['reservation']['data'] = data['reservation_data']
    board2['reservation']['avg'] = data['reservation_avg']

    board2['product_details_rate']['data'] = data['product_details_rate_data']
    board2['product_details_rate']['avg'] = data['product_details_rate_avg']

    board2['reservation_rate']['data'] = data['reservation_rate_data']
    board2['reservation_rate']['avg'] = data['reservation_rate_avg']

    return board1, board2


def get_chart(df_chart):
    chart1 = {
        'x': [], # 训练营付费人数近30天日期
        'y': [], # 训练营付费人数近30天数据
    }
    # 图表2
    chart2 = {
        'x': [], # DAU近30天日期
        'y': [], # DAU近30天数据
    }

    df_chart['date'] = df_chart['date'].apply( lambda date: date.strftime('%Y-%m-%d') )

    for index in df_chart.index:
        date = df_chart.loc[index, 'date']
        total_paying = int(df_chart.loc[index, 'total_paying'])
        dau = int(df_chart.loc[index, 'dau'])

        chart1['x'].append(date)
        chart2['x'].append(date)

        chart1['y'].append(total_paying)
        chart2['y'].append(dau)

    return chart1,chart2


# 日报数据接口
def daily_interface():
    ret_data = {}
    # 读数据
    df_board = pd.read_sql(sql['daily_board'], con=engine)
    df_chart = pd.read_sql(sql['daily_chart'], con=engine)
    # NAV
    date = df_board.loc[0, 'date'].strftime('%Y-%m-%d')
    weekday = weekday_transfer[
        df_board.loc[0, 'date'].weekday()
    ]
    ret_data['nav'] = {'date': date, 'weekday': weekday}
    # Board
    ret_data['board1'], ret_data['board2'] = get_board(df_board)
    # Chart
    ret_data['chart1'], ret_data['chart2'] = get_chart(df_chart)
    # Json
    return json.dumps(ret_data)


# 周报数据接口
def weekly_interface():
    ret_data = {}
    # 读数据
    df_board = pd.read_sql(sql['weekly_board'], con=engine)
    df_chart = pd.read_sql(sql['weekly_chart'], con=engine)
    # NAV
    date = df_board.loc[0, 'date']
    date_start = date.strftime('%Y-%m-%d')
    date_end = (date + datetime.timedelta(days=6)).strftime('%Y-%m-%d')
    weekday = '周一 至 周日'
    ret_data['nav'] = {'date': '%s至%s' % (date_start,date_end), 'weekday': weekday}
    # Board
    ret_data['board1'], ret_data['board2'] = get_board(df_board)
    # Chart
    ret_data['chart1'], ret_data['chart2'] = get_chart(df_chart)
    return json.dumps(ret_data)



if __name__ == '__main__':
    print(daily_interface())
    print(weekly_interface())
