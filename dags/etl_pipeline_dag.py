from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="automotive_etl_pipeline",
    start_date=datetime(2024,1,1),
    schedule_interval=None,
    catchup=False
) as dag:

    extract = BashOperator(
        task_id="extract_data",
        bash_command="python /opt/airflow/project/src/extract.py"
    )

    transform = BashOperator(
        task_id="transform_data",
        bash_command="python /opt/airflow/project/src/transform.py"
    )

    load = BashOperator(
        task_id="load_data",
        bash_command="python /opt/airflow/project/src/load.py"
    )

    extract >> transform >> load