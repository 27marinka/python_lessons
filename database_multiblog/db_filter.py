from database_multiblog.db_multiblog import Author
from database_multiblog.db_multiblog import Post
from database_multiblog.db_multiblog import Blog
from database_multiblog.db_multiblog import Teg


def all_tegs_of_author(session, author_name):
    res = get_all_tegs_of_author(session, author_name)
    title = f"Все теги, которые использовал автор {author_name} :\n"
    res = return_list_of_results(res)
    return title + res


def all_authors_by_teg(session, teg_name):
    res = get_all_authors_by_teg(session, teg_name)
    title = f"Все авторы, которые использовали тег {teg_name} :\n"
    res = return_list_of_results(res)
    return title + res


def return_list_of_results(res):
    list_of_res = ""
    for itm in res:
        list_of_res += f'{itm[0]} , \n'
    return list_of_res


def get_all_tegs_of_author(session, author_name):

    all_tegs = session.query(Teg.name) \
        .join(Post.tegs) \
        .join(Blog) \
        .join(Author) \
        .filter(Author.name == author_name) \
        .distinct() \
        .order_by(Teg.name)

    return all_tegs


def get_all_authors_by_teg(session, teg_name):

    all_authors = session.query(Author.name) \
        .join(Blog.post, Blog.author) \
        .join(Post.tegs) \
        .filter(Teg.name == teg_name) \
        .distinct()

    return all_authors

