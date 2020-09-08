import mem_profile
import random
import time 

names = ['AJi', 'Amie', 'Zakariya', 'Aisha']
majors = ['Math', 'Physics', 'Engineering', 'CompSci']

#Compare list and generator 

print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil()))
def people_list(num_people):
    result = []
    for i in xrange(num_people):
        person = {
            'id': i, 
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil()))
def people_generator(num_people):
    for i in xrange(num_people):
        person = {
            'id' : i, 
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield(person)


t1 = time.clock()
people = people_list(1000000)
t2 = time.clock()

print('Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil()))
print('Took {} Seconds'.format(t2-t1))
