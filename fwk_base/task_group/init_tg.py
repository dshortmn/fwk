from airflow.providers.standard.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup
from fwk_common.env_setup import GetConfigPathInfo
from fwk_common.file_io import load_yaml
from fwk.common.date_fcns import date_dict


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
            # Make sure an empty string is not considered a sql statement
            sql_value = data.get("sql_query", None)
            if sql_value is not None:
                if sql_value == "":
                    sql_value = None
            if sql_value is not None:
                sql_query = data.get("sql_query", None)
            else:
                sql_query = ""
                # load from sql file if exists
                if sql_file:
                    with open(sql_file, "r") as sql_f:
                        sql_query = sql_f.read()
                else:
                    raise ValueError("No SQL query provided in config or SQL file.")
            print(f"SQL Query: {sql_query}")
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
        # initialize jinja dictionary with data data
        jinja_dict = date_dict()
    return init_group
