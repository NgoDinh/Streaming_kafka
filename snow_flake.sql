snowsql -u vungo -a xr41662.europe-west4.gcp

--step 1: create file format
create or replace file format myjsonformat type='JSON' strip_outer_array=true;

--step 2: create stage
create or replace stage my_json_stage file_format = myjsonformat;

--step 3: create table
create table userdetails(userjson variant);

--step 4: copy file to stage
put file:///Users/vu/Downloads/userdetails.json @my_json_stage auto_compress=true;

--step 5: copy file from stage to table
--note can create a pipe to copy file.
copy into userdetails from @my_json_stage/userdetails.json.gz file_format=myjsonformat on_error='skip_file';
-- other tool is stream: https://docs.snowflake.com/en/sql-reference/sql/create-stream, https://community.snowflake.com/s/article/ELT-Data-Pipelining-in-Snowflake-Data-Warehouse-using-Streams-and-Tasks

put file:///Users/vu/Downloads/rooms.csv @rooms_stage auto_compress=true;
copy into rooms from @rooms_stage/rooms.csv.gz file_format=mycsv on_error='skip_file';

put file:///Users/vu/Downloads/floors.csv @floors_stage auto_compress=true;
copy into floors from @floors_stage/floors.csv.gz file_format=mycsv on_error='skip_file';

create table "LargeDataTable" ("pickup_datetime" STRING, "dropoff_datetime" STRING, "Pickup_longitude" DOUBLE, "Pickup_latitude" DOUBLE, "Dropoff_longitude" DOUBLE, "Dropoff_latitude" DOUBLE, "Trip_distance" DOUBLE, "Fare_amount" DOUBLE);
put file:///Users/vu/Downloads/large.csv @large_stage auto_compress=true parallel=4;
copy into "LargeDataTable" from @large_stage/large.csv.gz file_format=mycsv on_error='skip_file';