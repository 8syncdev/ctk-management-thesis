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
    account_id = Column(String, unique=True)
    name = Column(String)
    email = Column(String, unique=True)
    role = Column(String, default='student')  # Added field to differentiate between teacher and student
    password = Column(String)
    path_img = Column(String, nullable=True)
    groups = relationship('Group', back_populates='account')
    thesis = relationship('Thesis', back_populates='account')

# Define the Task model
class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    group_id = Column(Integer, ForeignKey('group.id'))
    progress = Column(Float, default=0)
    deadline = Column(DateTime, default=datetime.datetime.now()) 

    group = relationship('Group', back_populates='tasks')
    thesis = relationship('Thesis', back_populates='task')

# Define the Group model
class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    account_id = Column(Integer, ForeignKey('account.id'))

    account = relationship('Account', back_populates='groups')
    tasks = relationship('Task', back_populates='group')
    thesis = relationship('Thesis', back_populates='group')

# Define the Thesis model
class Thesis(Base):
    __tablename__ = 'thesis'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('account.id'))
    task_id = Column(Integer, ForeignKey('task.id'))
    group_id = Column(Integer, ForeignKey('group.id'))
    technology_categories_id = Column(Integer, ForeignKey('technology_category.id'))
    name = Column(String)
    technology_category = Column(String)
    criteria = Column(String) # Combined from the criteria of the technology requirements in the thesis_requirements
    score = Column(Float, default=0)
    deadline = Column(DateTime, default=datetime.datetime.now())

    task = relationship('Task', back_populates='thesis')
    technology_categories = relationship('TechnologyCategory', secondary=thesis_technology_category_association, back_populates='thesis')
    account = relationship('Account', back_populates='thesis')
    group = relationship('Group', back_populates='thesis')
    thesis_requirements = relationship('ThesisRequirement', back_populates='thesis', foreign_keys='ThesisRequirement.thesis_id')

# Define the TechnologyCategory model
class TechnologyCategory(Base):
    __tablename__ = 'technology_category'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    thesis = relationship('Thesis', secondary=thesis_technology_category_association, back_populates='technology_categories')

# Define the TechnologyRequirement model
class TechnologyRequirement(Base):
    __tablename__ = 'technology_requirement'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)

    thesis_requirements = relationship('ThesisRequirement', back_populates='technology_requirement')

# Define the ThesisRequirement model
class ThesisRequirement(Base):
    __tablename__ = 'thesis_requirement'

    id = Column(Integer, primary_key=True)
    thesis_id = Column(Integer, ForeignKey('thesis.id'))
    technology_requirement_id = Column(Integer, ForeignKey('technology_requirement.id'))

    thesis = relationship('Thesis', back_populates='thesis_requirements')
    technology_requirement = relationship('TechnologyRequirement', back_populates='thesis_requirements')

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
