# KEEP SCROLLING
from collections import namedtuple

# EDIT HERE

name='Szymon SIDOR'

mit = {
    'when': r'Jul 2010-Oct 2011',
    'where': r'Intech Inc',
    'role': r'Summer Intern',
    'image': 'mit.png',
    'description': r'Received pre-placed offer from the Exotics Trading Desk as a result of very positive review. Rated distinctive for Analytical Skills and Teamwork.',
}

events = [mit]

# DON'T EDIT BELOW THIS LINE
first_names = ' '.join(name.split(' ')[:-1])
last_name = name.split(' ')[-1].upper()

def table_multicell(items, align='r'):
    res = [r'\begin{tabular}{@{}%s@{}}' % (align,)]
    for i, item in enumerate(items):
        res.append('%s%s' % (item, r'' if i + 1 == len(items) else r'\\'))
    res.append(r'\end{tabular}')
    return ''.join(res)

