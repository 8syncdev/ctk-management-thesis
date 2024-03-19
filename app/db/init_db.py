from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import datetime
from app.setting.setting import BASE_DIR

# Create a declarative base
Base = declarative_base()

# Define the association table for the many-to-many relationship between Thesis and TechnologyCategory
thesis_technology_category_association = Table(
    'thesis_technology_category_association',
    Base.metadata,
    Column('thesis_id', Integer, ForeignKey('thesis.id')),
    Column('technology_category_id', Integer, ForeignKey('technology_category.id'))
)

# Define the Account model
class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    role = Column(String, default='student')  # Added field to differentiate between teacher and student
    password = Column(String)
    path_img = Column(String, nullable=True)
    # Define the one-to-many relationship between Account and Group
    group = relationship('Group', back_populates='account')
    # Define the one-to-many relationship between Account and Thesis
    thesis = relationship('Thesis', back_populates='account')

# Define the Task model
class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    group_id = Column(Integer, ForeignKey('group.id'))
    progress = Column(Float, default=0)
    deadline = Column(DateTime, default=datetime.datetime.now()) 
    # Define the many-to-one relationship between Task and Group
    group = relationship('Group', back_populates='tasks')

# Define the Group model
class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    # Define the one-to-many relationship between Group and Account
    account_id = Column(Integer, ForeignKey('account.id'), unique=True)

    account = relationship('Account', back_populates='group')
    tasks = relationship('Task', back_populates='group')
    thesis = relationship('Thesis', back_populates='group')

# Define association table for the many-to-many relationship between Thesis and Criterion
thesis_criterion_association = Table(
    'thesis_criterion_association',
    Base.metadata,
    Column('thesis_id', Integer, ForeignKey('thesis.id')),
    Column('criterion_id', Integer, ForeignKey('criterion.id'))
)

# Define the Criterion model
class Criterion(Base):
    __tablename__ = 'criterion'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String, nullable=True)

    thesis_list = relationship('Thesis', secondary=thesis_criterion_association, back_populates='criteria_list')

# Define association table for the many-to-many relationship between Thesis and TechnologyRequirement
tech_requriment_thesis_association = Table(
    'tech_requriment_thesis_association',
    Base.metadata,
    Column('thesis_id', Integer, ForeignKey('thesis.id')),
    Column('technology_requirement_id', Integer, ForeignKey('technology_requirement.id'))
)

# Define the Thesis model
class Thesis(Base):
    __tablename__ = 'thesis'

    id = Column(Integer, primary_key=True)
    # Define the one-to-many relationship between Thesis and Account
    account_id = Column(Integer, ForeignKey('account.id'), unique=True)
    # Define the one-to-many relationship between Thesis and Group
    group_id = Column(Integer, ForeignKey('group.id'), unique=True)
    name = Column(String)
    score = Column(Float, default=0)
    deadline = Column(DateTime, default=datetime.datetime.now())

    technology_category_list = relationship('TechnologyCategory', secondary=thesis_technology_category_association, back_populates='thesis_list')

    account = relationship('Account', back_populates='thesis')

    group = relationship('Group', back_populates='thesis')

    criteria_list = relationship('Criterion', secondary=thesis_criterion_association, back_populates='thesis_list')

    technology_requirement_list = relationship('TechnologyRequirement', secondary=tech_requriment_thesis_association, back_populates='thesis_list')



# Define the TechnologyCategory model
class TechnologyCategory(Base):
    __tablename__ = 'technology_category'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    thesis_list = relationship('Thesis', secondary=thesis_technology_category_association, back_populates='technology_category_list')

# Define the TechnologyRequirement model
class TechnologyRequirement(Base):
    __tablename__ = 'technology_requirement'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)

    thesis_list = relationship('Thesis', secondary=tech_requriment_thesis_association, back_populates='technology_requirement_list')





# Create the engine and connect to the SQLite database
engine = create_engine('sqlite:///' + str(BASE_DIR / 'thesis_management.sqlite3'))
Base.metadata.create_all(engine)

# Bind the engine to the Base
Base.metadata.bind = engine

# Create a sessionmaker to create sessions
Session = sessionmaker(bind=engine)

# Create the session
session = Session()

def connect_to_db():
    return session
