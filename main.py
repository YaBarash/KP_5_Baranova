from utils.utils import create_database, create_tables, insert_data_to_table

db_name = "kp_baranova"
create_database(db_name)
create_tables(db_name)
insert_data_to_table(db_name)
