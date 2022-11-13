from typing import List

from sqlalchemy.orm import Session


# DB operations
def create_db(db: Session, db_name: str):
    db.execute(f"CREATE DATABASE {db_name}")


def delete_db(db: Session, db_name: str):
    db.execute(f"DROP DATABASE {db_name}")


def get_tables(db: Session) -> List[str]:
    return db.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'").fetchall()


# Table operations
def create_table(db: Session, table_name: str, columns: List[str]):
    db.execute(f"CREATE TABLE {table_name} ({','.join(columns)})")


def delete_table(db: Session, table_name: str):
    db.execute(f"DROP TABLE {table_name}")


def update_table(db: Session, table_name: str, columns: List[str]):
    db.execute(f"ALTER TABLE {table_name} ADD {','.join(columns)}")


def get_columns(db: Session, table_name: str) -> List[str]:
    return db.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'").fetchall()


def get_all_records(db: Session, table_name: str) -> List[str]:
    return db.execute(f"SELECT * FROM {table_name}").fetchall()


# Record operations
def add_record(db: Session, table_name: str, values: List[str]):
    db.execute(f"INSERT INTO {table_name} VALUES ({','.join(values)})")


def delete_record(db: Session, table_name: str, id: int):
    db.execute(f"DELETE FROM {table_name} WHERE id = {id}")


def update_record(db: Session, table_name: str, id: int, values: List[str]):
    db.execute(f"UPDATE {table_name} SET {','.join(values)} WHERE id = {id}")


def get_record(db: Session, table_name: str, id: int) -> List[str]:
    return db.execute(f"SELECT * FROM {table_name} WHERE id = {id}").fetchall()


