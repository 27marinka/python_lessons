from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_multiblog import db_multiblog
from database_multiblog.db_autofill import fill_multiblog_db
from database_multiblog.db_filter import all_tegs_of_author, all_authors_by_teg


class DataBase:

    def __init__(self, db_url):
        engine = create_engine(db_url)
        db_multiblog.Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)


def get_filtered_results(db):
    session = db.maker()
    author_name = "Author_55"
    print(all_tegs_of_author(session, author_name))
    teg_name = "blogteg_33"
    print(all_authors_by_teg(session, teg_name))
    session.close


def main():
    db_url = "sqlite:///multiblog_db.db"
    db = DataBase(db_url)
    fill_multiblog_db(db)

    get_filtered_results(db)


if __name__ == '__main__':
    main()




