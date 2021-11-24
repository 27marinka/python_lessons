import random

from sqlalchemy.sql.expression import func

from database_multiblog import db_multiblog


def fill_multiblog_db(db):
    session = db.maker()
    # adding 100 tags
    for i in range(100):
        teg = db_multiblog.Teg(name=f"blogteg_{i}")
        session.add(teg)

    session.commit()

    for i in range(100):
        # creating 100 authors
        author = db_multiblog.Author(
            name=f'Author_{i}',
            nick=f'Nick_{i}',
            location="Moscow",
            rating=random.randint(1, 5))
        # creating 100 blogs
        blog = db_multiblog.Blog(
            name=f'Blog_{i}',
            rating=random.randint(1, 5),
            author_id=i)
        # tie up blog with author
        blog.author = author
        session.add(author)

        for j in range(random.randint(3, 10)):
            # adding 3 - 10 publications
            post = db_multiblog.Post(
                name=f'Чем кормить кота весной {j}',
                text=f'jdss sddsf sff {j}',
                author_id=i,
                blog_id=i)

            # select 3 - 5 tags from db
            tegs = session.query(db_multiblog.Teg)\
                .order_by(func.random())\
                .limit(random.randint(3, 5))\
                .all()

            # add tags to publication
            post.tegs.extend(tegs)

            # tie up publication with blog
            blog.post.append(post)

            session.add(post)
            session.commit()

        session.add(blog)
        session.commit()

    session.close()


