select channel, count(*)
from support_tickets_processed
group by channel

select status, count(*)
from support_tickets_processed
group by status

select agent, count(*)
from support_tickets_processed
group by agent

select log_level, count(*) as event_count
from support_logs_processed
group by log_level
order by event_count desc

select 
    date(created_at) as day,
    count(*) as events
from support_tickets_processed
group by date(created_at)
order by events desc

select 
    user_agent,
    avg(cpu) as cpu_usage
from support_logs_processed
group by user_agent
order by cpu_usage desc