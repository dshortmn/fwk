from airflow.providers.standard.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup
from fwk_common.env_setup import GetConfigPathInfo
from fwk_common.file_io import load_yaml


def init_data_tg(group_id: str) -> TaskGroup:
    """
    Defines a TaskGroup for initialization of framework.
    """
    with TaskGroup(group_id=group_id) as init_group:

        def init_task(**kwargs):
            """
            initialization logic.
            This function initialization steps for framework..
            """
            dag_filepath = kwargs["dag"].fileloc
            config_file, sql_file = GetConfigPathInfo(dag_filepath)
            data = load_yaml(config_file)
            # generate date replacement logic

            # jinji

            print(f"DAG file path: {dag_filepath}")
            print(f"{kwargs=}")
            config_file, sql_file = GetConfigPathInfo(dag_filepath)
            print(f"     Config file: {config_file}")
            print(f"     Sql file: {sql_file}")
            data = load_yaml(config_file)
            print(f"Data loaded from config file: {data}")
            print("Initialization task executed.")

        init_process = PythonOperator(task_id="init_process", python_callable=init_task)

        init_process  # Define internal dependency
    return init_group
