from contextlib import contextmanager, AbstractContextManager
from typing import Callable
import logging
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, orm
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)

Base = declarative_base()


class Database:

    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(db_url, echo=True)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()






""" from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

def session_maker_function():
    # Configura la conexión a tu base de datos MySQL
    db_url = 'mysql+pymysql://root:irda0205@localhost/miresto'
    engine = create_engine(db_url)

    # Crea una clase de fábrica de sesiones
    Session = sessionmaker(bind=engine)

    # Retorna una instancia de sesión
    return Session()


Base = declarative_base()

 """