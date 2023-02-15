import sqlalchemy
import enum
from sqlalchemy import Column, ForeignKey, String, Integer, Float, Enum, DateTime, Boolean, Text, Date
from database import metadata, engine


# Enum class
class Role(enum.Enum):
    admin = "ADMIN"
    common = "COMMON"

class ValueType(enum.Enum):
    number = "NUMBER"
    multiple = "ORDINAL_ENUM"
    ordered_multiple = "CATEGORICAL_ENUM"
    text = "TEXT"
    date = "DATE"

class OptimizeType(enum.Enum):
    minimize = "MINIMIZE"
    maximize = "MAXIMIZE"


class Metric(enum.Enum):
    moreThan = ">="
    lessThan = "<="
    equalTo = "=="
   
class Pricing(enum.Enum):
    simple = "FREE"
    advanced = "PREMIUM"

users = sqlalchemy.Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(64)),
    Column("email", String, nullable=False, unique = True),
    Column("password", String(256)),
    Column("role", Enum(Role), default=Role.common),
    Column('pricing', Enum(Pricing), default = Pricing.simple),
    Column("verified", Boolean, nullable=False, default='False'),
    Column("verification_code", String, nullable=True, unique=True),
    Column("active", Boolean, default=True),
    Column("created_at", DateTime),
)

candidates_files = sqlalchemy.Table(
    "candidatesFiles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("zip_path", String, nullable=True),
    Column("data_path", String, nullable=True),
    Column("extension", String(5), nullable=True),
    Column("performed_cleaning", String(256), nullable=True),
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE")),
)

selection_files = sqlalchemy.Table(
    "selectionFiles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("encoded_file", Text, nullable=False),
    Column("status", String),
    Column("nb_sol", Integer),
    Column("satisfaction", Integer, nullable=True),
    Column("features", Text, nullable=False),
    Column("candidatesFile_id", Integer, ForeignKey("candidatesFiles.id", ondelete="CASCADE")),
)

features = sqlalchemy.Table(
    "features",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("label", String, nullable=False),
    Column("value_type", Enum(ValueType), nullable=False),
    Column("candidatesFile_id", Integer, ForeignKey("candidatesFiles.id", ondelete="CASCADE")),
)

number_constraints = sqlalchemy.Table(
    "n_constraints",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("min_value", Float, nullable=True),
    Column("max_value", Float, nullable=True),
    Column("mean_value", Float, nullable=True),
    Column("coefficient", Float, nullable=True),
    Column("optimize", Enum(OptimizeType), nullable=True),
    Column("feature_id", Integer, ForeignKey("features.id", ondelete="CASCADE")),
)

enum_constraints = sqlalchemy.Table(
    "e_constraints",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("value", String, nullable=False),
    Column("number", Integer, nullable=False),
    Column("metric", Enum(Metric), nullable=False),
    Column("weight", Integer, nullable=True),
    Column("optimize", Enum(OptimizeType), nullable=True),
    Column("feature_id", Integer, ForeignKey("features.id", ondelete="CASCADE")),
)

text_constraints = sqlalchemy.Table(
    "t_constraints",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("must_contain", String, nullable=False),
    Column("weight", Integer, nullable=True),
    Column("optimize", Enum(OptimizeType), nullable=True),
    Column("feature_id", Integer, ForeignKey("features.id", ondelete="CASCADE")),
)

date_constraints = sqlalchemy.Table(
    "t_constraints",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("min_date", Date, nullable=True),
    Column("max_date", Date, nullable=True),
    Column("optimize", Enum(OptimizeType), nullable=True),
    Column("feature_id", Integer, ForeignKey("features.id", ondelete="CASCADE")),
)

metadata.create_all(engine)