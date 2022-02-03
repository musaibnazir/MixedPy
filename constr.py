class student(object):
    def __init__(self):
        name=''
        age = 0
        stClass = ''

st = student()
setattr(st,'name','Adeel')
setattr(st,'age','12')
setattr(st,'stClass','abc')
print(getattr(st,'name'))
print(getattr(st,'age'))
print(getattr(st,'stClass'))
print(hasattr(st,'stClass'))
delattr(student,'name')
print(getattr(st,'name'))
