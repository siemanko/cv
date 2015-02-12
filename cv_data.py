# KEEP SCROLLING
from collections import namedtuple

# EDIT HERE

name='Szymon SIDOR'

email='szymon.sidor@gmail.com'
phone='+14438799664'
facebook='fb.com/szymon.sidor'

mit = {
    'when': r'January 2014 - Current',
    'where': r'Massachusetts Institute of Technology',
    'role': r'Computer Science PhD',
    'image': 'mit.png',
    'courses': [
        'Machine Learning (A)',
        'Underactuated Robotics (A)',
        'Integer Optimization (A)',
        'Computer and Network Security (A)',
    ],
    'extra_info': {
        'Research Interests': 'My research concerns applying machine learning techniques for Dialog Systems (think Siri solving more complex problems like planning your day). My academic adviser is Brian Williams.',
        'Research Assistantship': 'My PhD is sponsored by TATA Center at MIT. Part of my research involves traveling to rural areas in India and deploying my algorithms on village scale power microgrid.',
    },
}

cambridge = {
    'when': r'Jul 2010-Oct 2011',
    'where': r'Intech Inc',
    'role': r'Summer Intern',
    'image': 'mit.png',
    'extra_info' : {}
}

events = [mit, cambridge]

# DON'T EDIT BELOW THIS LINE
first_names = ' '.join(name.split(' ')[:-1])
last_name = name.split(' ')[-1].upper()

def table_multicell(items, align='r'):
    res = [r'\begin{tabular}{@{}%s@{}}' % (align,)]
    for i, item in enumerate(items):
        res.append('%s%s' % (item, r'' if i + 1 == len(items) else r'\\'))
    res.append(r'\end{tabular}')
    return ''.join(res)

