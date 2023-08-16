# * Создать базу данных для хранения информации о студентах и их оценках в
# учебном заведении.
# * База данных должна содержать две таблицы: "Студенты" и "Оценки".
# * В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
# * В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
# * Необходимо создать связь между таблицами "Студенты" и "Оценки".

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(30), nullable=False)
    ratings = db.relationship('Rating', backref='student', lazy=True)
    
    def __repr__(self):
        return f'Student({self.name}, {self.surname}, {self.group}, {self.email})'


# В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    sub_study = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'Rating({self.student_id}, {self.sub_study}, {self.rating})'
    