  SELECT * 
  FROM {{source_schema}}.{{source_table}} 
  WHERE partition_column = to_date('{{nodash_curr_date}}', 'YYYYMMDD')
    AND id > {{last_id}}
  ORDER BY id
  LIMIT 1000;