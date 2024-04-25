from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime, Table, text
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
# Define association table for the many-to-many relationship between Account and Group
account_group_association = Table(
    'account_group_association',
    Base.metadata,
    Column('account_id', Integer, ForeignKey('account.id')),
    Column('group_id', Integer, ForeignKey('group.id'))
)

# Define association table for the many-to-many relationship between Task and Account
task_account_association = Table(
    'task_account_association',
    Base.metadata,
    Column('task_id', Integer, ForeignKey('task.id')),
    Column('account_id', Integer, ForeignKey('account.id'))
)

# Define association table for the many-to-many relationship between GradeByCouncil and Account
grade_by_council_account_association = Table(
    'grade_by_council_account_association',
    Base.metadata,
    Column('grade_by_council_id', Integer, ForeignKey('grade_by_council.id')),
    Column('account_id', Integer, ForeignKey('account.id'))
)

# Define the Account model
class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    role = Column(String, default='student')  # Added field to differentiate between teacher and student
    password = Column(String)
    path_img = Column(String, nullable=True)
    # Define the one-to-many relationship between Account and Group
    group_list = relationship('Group', secondary=account_group_association, back_populates='account_list')
    # Define the one-to-many relationship between Account and Thesis
    thesis = relationship('Thesis', back_populates='account')
    # Define the many-to-many relationship between Task and Account
    task_list = relationship('Task', secondary=task_account_association, back_populates='account_list')
    # Define the one-to-many relationship between GradeByCouncil and Account
    grade_by_council_list = relationship('GradeByCouncil', secondary=grade_by_council_account_association, back_populates='account_list')

# Define association table for the many-to-many relationship between Thesis and Group
group_thesis_association = Table(
    'group_thesis_association',
    Base.metadata,
    Column('thesis_id', Integer, ForeignKey('thesis.id')),
    Column('group_id', Integer, ForeignKey('group.id'))
)


# Define association table for the many-to-many relationship between Task and Comment
task_comment_association = Table(
    'task_comment_association',
    Base.metadata,
    Column('task_id', Integer, ForeignKey('task.id')),
    Column('comment_id', Integer, ForeignKey('comment.id'))
)

# Define association table for the many-to-many relationship between Group and Task
group_task_association = Table(
    'group_task_association',
    Base.metadata,
    Column('group_id', Integer, ForeignKey('group.id')),
    Column('task_id', Integer, ForeignKey('task.id'))
)


# Define the Task model
class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    progress = Column(Float, default=0)
    deadline = Column(DateTime, default=datetime.datetime.now()) 
    # Define the many-to-many relationship between Task and Account
    account_list = relationship('Account', secondary=task_account_association, back_populates='task_list')
    # Define the many-to-many relationship between Task and Comment
    comment_list = relationship('Comment', secondary=task_comment_association, back_populates='task_list')
    # Define the many-to-many relationship between Group and Task
    group_list = relationship('Group', secondary=group_task_association, back_populates='task_list')

# Define the Group model
class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    # Define the one-to-many relationship between Group and Account
    account_id = Column(Integer, ForeignKey('account.id'), unique=True)

    account_list = relationship('Account', secondary=account_group_association, back_populates='group_list')
    thesis_list = relationship('Thesis', secondary=group_thesis_association, back_populates='group_list')
    # Define the many-to-many relationship between Group and Task
    task_list = relationship('Task', secondary=group_task_association, back_populates='group_list')

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
    name = Column(String)
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
    # Define the many-to-many relationship between Thesis and Account
    account_id = Column(Integer, ForeignKey('account.id'))
    # Define the one-to-many relationship between Thesis and Group
    group_id = Column(Integer, ForeignKey('group.id'), unique=True)
    name = Column(String)
    score = Column(Float, default=0)
    deadline = Column(DateTime, default=datetime.datetime.now())

    technology_category_list = relationship('TechnologyCategory', secondary=thesis_technology_category_association, back_populates='thesis_list')

    account = relationship('Account', back_populates='thesis')

    group_list = relationship('Group', secondary=group_thesis_association, back_populates='thesis_list')

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
    name = Column(String)
    description = Column(String)

    thesis_list = relationship('Thesis', secondary=tech_requriment_thesis_association, back_populates='technology_requirement_list')

# Define the Comment model
class Comment (Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())
    # Define the one-to-many relationship between Comment and Account
    account_id = Column(Integer, ForeignKey('account.id'))

    account = relationship('Account')
    task_list = relationship('Task', secondary=task_comment_association, back_populates='comment_list')

# Define the Grade model
class Grade(Base):
    __tablename__ = 'grade'

    id = Column(Integer, primary_key=True)
    score = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.now())
    # Define the one-to-many relationship between Grade and Account
    account_id = Column(Integer, ForeignKey('account.id'))
    # Define the one-to-many relationship between Grade and Thesis
    thesis_id = Column(Integer, ForeignKey('thesis.id'))

    account = relationship('Account')
    thesis = relationship('Thesis')



# Grade by council
class GradeByCouncil(Base):
    __tablename__ = 'grade_by_council'
    id = Column(Integer, primary_key=True)
    thesis_id = Column(Integer, ForeignKey('thesis.id'))

    thesis = relationship('Thesis')
    account_list = relationship('Account', secondary=grade_by_council_account_association, back_populates='grade_by_council_list')





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
