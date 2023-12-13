#Different behaviours of strings
course = 'Python for beginners'
course = "Python for 'beginners'"
course = 'Python for "beginners"'
email = '''
Hi Subrata,
Here is my first email to you via "Python".
Thank you!
The DevOps Support team!
'''
print (course)
print (course.upper())
print (course.lower())
print (course.find('y'))
print (course.find('Y'))
print (course.find('for'))
print (course.replace('for', '4'))
print (course.replace('x', '4'))
print (course.replace('beginners', 'Absolute beginners'))
print (course.find('Python'))
print ('Python' in course)
print ('python' in course)

print(email)

print(len(course))

print(course.title())

#o/p
#Python for "beginners"
#PYTHON FOR "BEGINNERS"
#python for "beginners"
#1
#-1
#7
#Python 4 "beginners"
#Python for "beginners"
#Python for "Absolute beginners"
#0
#True
#False

#Hi Subrata,
#Here is my first email to you via "Python".
#Thank you!
#The DevOps Support team!

#22
#Python For "Beginners"
