import logging
import psycopg2
from psycopg2 import Error
import os

rds_host = os.environ['DB_ENDPOINT']
rds_port = os.environ['DB_PORT']
rds_username = os.environ['DB_USER']
rds_password = os.environ['DB_PASSWORD']

logger = logging.getLogger("Run-Lambda")
logger.setLevel(logging.INFO)

try:
    conn = psycopg2.connect(host=rds_host, port=rds_port, user=rds_username, password=rds_password)
except (Exception, Error) as error:
    logger.error("ERROR: Unexpected error: Could not connect to Postgres instance.", error)

logger.info("SUCCESS: Connection to RDS Postgres instance succeeded")

def handler(event, context):
    """
    This function fetches content from Postgres RDS instance
    """

    item_count = 0

    with conn.cursor() as cur:
        cur.execute("drop table pet")
        cur.execute("create table pet (id bigint primary key, name varchar(255) not null, birth_date timestamp not null, tutor_name varchar(255) not null)")
        conn.commit()

        cur.execute("select * from pet")
        for row in cur:
            item_count += 1
            logger.info(row)
        conn.commit()

    return "Added %d items from RDS Postgres table" %(item_count)
