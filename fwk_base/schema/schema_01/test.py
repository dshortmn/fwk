from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from fwk_common.env_setup import GetConfigPathInfo
from fwk_common.file_io import load_yaml
from pendulum import today

from fwk_base.task_group.init_tg import init_data_tg

with DAG(
    dag_id="example_task_group",
    start_date=today("UTC").add(days=-2),
    schedule=None,
    tags=["example"],
) as dag:
    start_task = BashOperator(task_id="start_task", bash_command="echo 'Starting DAG'")

    # Instantiate the TaskGroup using the imported function.
    my_task_group_instance = init_data_tg("my_task_group")

    end_task = BashOperator(task_id="end_task", bash_command="echo 'DAG finished'")

    # Define dependencies involving the TaskGroup
    start_task >> my_task_group_instance >> end_task


if __name__ == "__main__":
    print(f"{__file__=}")
    config_file, sql_file = GetConfigPathInfo()
    print(f"     Config file: {config_file}")
    print(f"     Sql file: {sql_file}")
    config_file, sql_file = GetConfigPathInfo(__file__)
    print(f"Pass Config file: {config_file}")
    print(f"Pass Sql file: {sql_file}")
    data = load_yaml(config_file)
    print(f"Data loaded from config file: {data}")
