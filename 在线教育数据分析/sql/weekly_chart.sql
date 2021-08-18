select 当周周一    as date,
       总付费人数 as total_paying,
       DAU   as dau
from 周报
order by 当周周一 desc
limit 30;