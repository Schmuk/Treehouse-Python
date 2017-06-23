from peewee import *  # convention for working with peewee

db = SqliteDatabase('students.db')


class Student(Model):  # models always named with singular name
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)
    
    class Meta:  # tells model what database it belongs to
        database = db
        
        
students = [
    {'username': 'cjhfitz',
    'points': 14718},
    {'username': 'chalkers',
    'points': 11912},
    {'username': 'joykesten2',
    'points': 7363},
    {'username': 'craigsdennis',
    'points': 4079},
    {'username': 'davidmcfarland',
    'points': 14717}
]

def add_students():
    try:
        for student in students:
            Student.create(username=student['username'], points=student['points'])
    except IntegrityError:  # updates
        student_record = Student.get(username=student['username'])
        student_record.points = student['points']
        student_record.save()
            
def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    # get all the students, sort them from most points to least, then get first record
    return student

            
if __name__ == '__main__':  # if file is run directly and not imported
    db.connect()  # connect to database
    db.create_tables([Student], safe=True)  # create tables (Student table)
    add_students()
    print("Our top student right now is: {0.username}".format(top_student()))  # {0.username} 0 is whatever is returned from top_student(), username is the attribute
    