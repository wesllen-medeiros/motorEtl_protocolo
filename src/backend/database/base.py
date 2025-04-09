from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

# Individualizar sistemas

BASE_ADMIN = declarative_base(metadata=MetaData(schema='admin'))
BASE_FOLHA = declarative_base(metadata=MetaData(schema='folha'))