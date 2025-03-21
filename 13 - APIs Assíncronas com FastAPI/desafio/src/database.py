import databases
import sqlalchemy as sa

from src.config import settings

# Inicializa o objeto de banco de dados usando a URL de configuração.
database = databases.Database(settings.database_url)

# Inicializa os metadados do SQLAlchemy.
metadata = sa.MetaData()

# Cria a engine do SQLAlchemy com base no ambiente configurado.
if settings.environment == "production":
    # Em produção, a conexão é direta.
    engine = sa.create_engine(settings.database_url)
else:
    # Em desenvolvimento ou testes, desativa a verificação de threads.
    engine = sa.create_engine(settings.database_url, connect_args={"check_same_thread": False})

