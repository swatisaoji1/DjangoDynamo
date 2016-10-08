from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute, NumberAttribute
# Create your models here.


class Student(Model):
    class Meta:
        table_name = 'students'
        region = 'us-west-1'
        host = 'https://dynamodb.us-west-1.amazonaws.com'
        write_capacity_units = 1
        read_capacity_units = 1

    student_id = UnicodeAttribute(hash_key=True)
    email = UnicodeAttribute()
    first_name = UnicodeAttribute()
    last_name = UnicodeAttribute()
    address = UnicodeAttribute()
    gpa = NumberAttribute()