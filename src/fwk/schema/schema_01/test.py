from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from fwk_common.env_setup import GetCommonPath
from pendulum import today
from task_group.tg1 import create_my_task_group

with DAG(
    dag_id="example_task_group", start_date=today("UTC").add(days=-2), tags=["example"]
) as dag:
    start_task = BashOperator(task_id="start_task", bash_command="echo 'Starting DAG'")

    # Instantiate the TaskGroup using the imported function
    my_task_group_instance = create_my_task_group("my_task_group")

    end_task = BashOperator(task_id="end_task", bash_command="echo 'DAG finished'")

    # Define dependencies involving the TaskGroup
    start_task >> my_task_group_instance >> end_task


if __name__ == "__main__":
    current_directory = GetCommonPath()

    print(f"{current_directory=}")
