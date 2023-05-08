import os
from application import app, db
from application.models.models import User, UserSetting, Task, Message, Token, Sensory


def delete_database():
    with app.app_context():
        db.drop_all()

def create_database():
    with app.app_context():
        db.create_all()

def add_entries():
    User1 = User(username='test', email='test@test.com', password='test')

    Setting1 = UserSetting(user_id=1, colour_scheme=2, push_notifications=1, font_name='Poppins', font_size='Medium', points=50)

    Task1 = Task(user_id=1, category_name='Python', task_name='Python testing', task_url='https://realpython.com/python-testing/', task_desc='Try and understand the concept of unit testing with Python')
    Task2 = Task(user_id=1, category_name='Django', task_name='Django intro', task_url='https://www.w3schools.com/django/django_intro.php', task_desc='Start on Django')
    Task3 = Task(user_id=1, category_name='Design', task_name='Design plans', task_url='None', task_desc='Find some designs for a portfolio website')

    Message1 = Message(user_id=1, date='2023-02-26 23:59:16', content='Hi and welcome to Focalise!')
    Message2 = Message(user_id=1, date='2023-02-26 23:59:16', content='This is a test message')

    Token1 = Token(user_id=1, token='f1e7c715-215d-43a7-ac45-bea3c9d423a2')

    Sensory1 = Sensory(sensory_id=1, video_category='Music', video_url='https://www.youtube.com/watch?v=zuCRSwWssVk')
    Sensory2 = Sensory(sensory_id=6, video_category='Animals', video_url='https://www.youtube.com/watch?v=3szkFHfr6sA')
    Sensory3 = Sensory(sensory_id=11, video_category='Meditation', video_url='https://www.youtube.com/watch?v=itZMM5gCboo')

    with app.app_context():
        db.session.add(User1)
        db.session.add(Setting1)
        db.session.add(Task1)
        db.session.add(Task2)
        db.session.add(Task3)
        db.session.add(Message1)
        db.session.add(Message2)
        db.session.add(Token1)
        db.session.add(Sensory1)
        db.session.add(Sensory2)
        db.session.add(Sensory3)
        db.session.commit()

def see_db_entries():
    print("Test database created")
    # with app.app_context():
    #     users = User.query.all()
    #     for user in users:
    #         print(f"{user.username}, {user.email}, {user.password}")
    #     settings = UserSetting.query.all()
    #     for setting in settings:
    #         print(f"{setting.colour_scheme}")
    #     tasks = Task.query.all()
    #     for task in tasks:
    #         print(f"{task.category_name}, {task.task_name}, {task.task_desc}")
    #     messages = Message.query.all()
    #     for message in messages:
    #         print(f"{message.date}, {message.content}")
    #     tokens = Token.query.all()
    #     for token in tokens:
    #         print(f"{token.token}")
    #     sensorys = Sensory.query.all()
    #     for sensory in sensorys:
    #         print(f"{sensory.video_category}")

if __name__ == '__main__':
    delete_database()
    create_database()
    add_entries()
    see_db_entries()
