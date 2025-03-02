# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, LargeBinary, SmallInteger, String, Text
from sqlalchemy.schema import FetchedValue
from sqlalchemy.dialects.mysql.enumerated import ENUM
from flask_sqlalchemy import SQLAlchemy
from application import db

db = SQLAlchemy()

# flask-sqlacodegen "mysql://root:root@127.0.0.0.1/mysql" --tables user --outfile "./common/models/user.py" --flask


class User(db.Model):
    __tablename__ = 'user'

    Host = db.Column(db.String(60, 'utf8_bin'), primary_key=True, nullable=False, server_default=db.FetchedValue())
    User = db.Column(db.String(32, 'utf8_bin'), primary_key=True, nullable=False, server_default=db.FetchedValue())
    Select_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Insert_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Update_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Delete_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Create_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Drop_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Reload_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Shutdown_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Process_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    File_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Grant_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    References_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Index_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Alter_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Show_db_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Super_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Create_tmp_table_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Lock_tables_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Execute_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Repl_slave_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Repl_client_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Create_view_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Show_view_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Create_routine_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Alter_routine_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Create_user_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Event_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Trigger_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    Create_tablespace_priv = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    ssl_type = db.Column(db.ENUM('', 'ANY', 'X509', 'SPECIFIED'), nullable=False, server_default=db.FetchedValue())
    ssl_cipher = db.Column(db.LargeBinary, nullable=False)
    x509_issuer = db.Column(db.LargeBinary, nullable=False)
    x509_subject = db.Column(db.LargeBinary, nullable=False)
    max_questions = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    max_updates = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    max_connections = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    max_user_connections = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    plugin = db.Column(db.String(64, 'utf8_bin'), nullable=False, server_default=db.FetchedValue())
    authentication_string = db.Column(db.Text(collation='utf8_bin'))
    password_expired = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
    password_last_changed = db.Column(db.DateTime)
    password_lifetime = db.Column(db.SmallInteger)
    account_locked = db.Column(db.ENUM('N', 'Y'), nullable=False, server_default=db.FetchedValue())
