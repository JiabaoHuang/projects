select
    日期 as date,
    总付费人数 as total_paying,
    DAU as dau
from 日报
order by 日期 desc
limit 30
;