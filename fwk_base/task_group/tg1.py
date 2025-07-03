from airflow.utils.task_group import TaskGroup
from airflow.providers.standard.operators.empty import EmptyOperator


def create_my_task_group(group_id: str) -> TaskGroup:
    """
    Defines a TaskGroup with sample tasks.
    """
    with TaskGroup(group_id=group_id) as my_group:
        task_1 = EmptyOperator(task_id="task_1")
        task_2 = EmptyOperator(task_id="task_2")
        task_1 >> task_2  # Define internal dependency
    return my_group
