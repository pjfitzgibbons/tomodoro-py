from sqlalchemy.orm import registry

_mapper_registry = registry()

metadata = _mapper_registry.metadata
Base = _mapper_registry.generate_base()

__ALL__ = [metadata, Base]