with p as
         (select 当周周一                          as date,
                 ifnull(总付费人数, 0)            as 'total_paying',
                 ifnull(付费人数_训练营, 0)         as 'training_camp',
                 ifnull(付费人数_专栏, 0)          as 'special_column',
                 ifnull(付费人数_会员, 0)          as 'vip_member',
                 ifnull(激活人数, 0)             as 'activate_user',
                 ifnull(DAU, 0)              as 'dau',
                 ifnull(客单价, 0)              as 'customer_price',
                 ifnull(总付费金额, 0)            as 'amount',
                 ifnull(新用户次日留存率, 0)         as 'new_customer_remain_day',
                 ifnull(新用户7日留存率, 0)         as 'new_customer_remain_week',
                 ifnull(活跃用户次日留存率, 0)        as 'active_customer_remain_day',
                 ifnull(活跃用户7日留存率, 0)        as 'active_customer_remain_week',
                 ifnull(浏览商详人数_训练营, 0)       as 'product_details',
                 ifnull(`预约-付费转化率_训练营`, 0)   as 'reservation',
                 ifnull(`浏览商详-预约转化率_训练营`, 0) as 'product_details_rate',
                 ifnull(`预约-付费转化率_训练营`, 0)   as 'reservation_rate'
          from 周报
          order by 当周周一 desc
          limit 30)

select current.date                                                                                                as date,
       current.total_paying                                                                                        as total_paying_num,
       if(last_2.total_paying = 0, last_1.total_paying, (last_1.total_paying - last_2.total_paying) /
                                                        last_2.total_paying)                                       as total_paying_rate_day,
       if(last_7.total_paying = 0, current.total_paying, (current.total_paying - last_7.total_paying) /
                                                         last_7.total_paying)                                      as total_paying_rate_week,
       current.training_camp                                                                                       as training_camp_num,
       if(last_2.training_camp = 0, last_1.training_camp, (last_1.training_camp - last_2.training_camp) /
                                                          last_2.training_camp)                                    as training_camp_rate_day,
       if(last_7.training_camp = 0, current.training_camp, (current.training_camp - last_7.training_camp) /
                                                           last_7.training_camp)                                   as training_camp_rate_week,

       current.special_column                                                                                      as special_column_num,
       if(last_2.special_column = 0, last_1.special_column, (last_1.special_column - last_2.special_column) /
                                                            last_2.special_column)                                 as special_column_rate_day,
       if(last_7.special_column = 0, current.special_column, (current.special_column - last_7.special_column) /
                                                             last_7.special_column)                                as special_column_rate_week,

       current.vip_member                                                                                          as vip_member_num,
       if(last_2.vip_member = 0, last_1.vip_member, (last_1.vip_member - last_2.vip_member) /
                                                    last_2.vip_member)                                             as vip_member_rate_day,
       if(last_7.vip_member = 0, current.vip_member, (current.vip_member - last_7.vip_member) /
                                                     last_7.vip_member)                                            as vip_member_rate_week,

       current.activate_user                                                                                       as activate_user_num,
       if(last_2.activate_user = 0, last_1.activate_user, (last_1.activate_user - last_2.activate_user) /
                                                          last_2.activate_user)                                    as activate_user_rate_day,
       if(last_7.activate_user = 0, current.activate_user, (current.activate_user - last_7.activate_user) /
                                                           last_7.activate_user)                                   as activate_user_rate_week,

       current.dau                                                                                                 as dau_num,
       if(last_2.dau = 0, last_1.dau, (last_1.dau - last_2.dau) /
                                      last_2.dau)                                                                  as dau_rate_day,
       if(last_7.dau = 0, current.dau, (current.dau - last_7.dau) /
                                       last_7.dau)                                                                 as dau_rate_week,

       current.customer_price                                                                                      as customer_price_num,
       if(last_2.customer_price = 0, last_1.customer_price, (last_1.customer_price - last_2.customer_price) /
                                                            last_2.customer_price)                                 as customer_price_rate_day,
       if(last_7.customer_price = 0, current.customer_price, (current.customer_price - last_7.customer_price) /
                                                             last_7.customer_price)                                as customer_price_rate_week,

       current.amount                                                                                              as amount_num,
       if(last_2.amount = 0, last_1.amount, (last_1.amount - last_2.amount) /
                                            last_2.amount)                                                         as amount_rate_day,
       if(last_7.amount = 0, current.amount, (current.amount - last_7.amount) /
                                             last_7.amount)                                                        as amount_rate_week,

       current.new_customer_remain_day                                                                             as new_customer_remain_day_data,
       f1.new_customer_remain_day_avg                                                                              as new_customer_remain_day_avg,

       current.new_customer_remain_week                                                                            as new_customer_remain_week_data,
       f1.new_customer_remain_week_avg                                                                             as new_customer_remain_week_avg,

       current.active_customer_remain_day                                                                          as active_customer_remain_day_data,
       f1.active_customer_remain_day_avg                                                                           as active_customer_remain_day_avg,

       current.active_customer_remain_week                                                                         as active_customer_remain_week_data,
       f1.active_customer_remain_week_avg                                                                          as active_customer_remain_week_avg,

       current.product_details                                                                                     as product_details_data,
       f1.product_details_avg                                                                                      as product_details_avg,

       current.reservation                                                                                         as reservation_data,
       f1.reservation_avg                                                                                          as reservation_avg,

       current.product_details_rate                                                                                as product_details_rate_data,
       f1.product_details_rate_avg                                                                                 as product_details_rate_avg,

       current.reservation_rate                                                                                    as reservation_rate_data,
       f1.reservation_rate_avg                                                                                     as reservation_rate_avg


from (select * from p) as current
         left join(select * from p) last_1 on datediff(current.date, last_1.date) = 1
         left join(select * from p) last_2 on datediff(current.date, last_2.date) = 2
         left join(select * from p) last_7 on datediff(current.date, last_7.date) = 7
         left join(select avg(new_customer_remain_day)     as new_customer_remain_day_avg,
                          avg(new_customer_remain_week)    as new_customer_remain_week_avg,
                          avg(active_customer_remain_day)  as active_customer_remain_day_avg,
                          avg(active_customer_remain_week) as active_customer_remain_week_avg,
                          avg(product_details)             as product_details_avg,
                          avg(reservation)                 as reservation_avg,
                          avg(product_details_rate)        as product_details_rate_avg,
                          avg(reservation_rate)            as reservation_rate_avg
                   from p
) f1 on 1 = 1
;
