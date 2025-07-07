  SELECT * 
  FROM {{source_schema}}.{{source_table}} 
  WHERE partition_column = {{current_date}}
  ORDER BY id
  LIMIT 1000;