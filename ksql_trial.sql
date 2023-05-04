-- access terminal of ksql server container and using "ksql" to using ksql
SHOW TOPICS; --to show all topics

-- get raw data
Create stream users(
    user_id INTEGER,
    user_name VARCHAR,
    user_address VARCHAR,
    platform VARCHAR,
    signup_at VARCHAR
)
with (kafka_topic = 'udacity.ex.topic_faust', value_format = 'json');

-- create stream based on another
create stream Mobile as select * from users where platform = 'Mobile';

-- create table
-- create table 
Create table test1(
    user_id INTEGER ,
    user_name VARCHAR PRIMARY KEY,
    user_address VARCHAR,
    platform VARCHAR,
    signup_at VARCHAR)
with (kafka_topic = 'udacity.ex.topic_faust', value_format = 'json');

-- get data from stream
select * from Mobile

-- set offet
SET 'auto.offset.reset' = 'earliest'
UNSET 'auto.offset.reset'