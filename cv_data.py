# KEEP SCROLLING
from collections import namedtuple

# EDIT HERE

name='Szymon SIDOR'

email='szymon.sidor@gmail.com'
phone='+14438799664'
facebook=r'\url{fb.com/szymon.sidor}'

mit = {
    'fixup': str(3.0),
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
    'projects': {
        r'Android Security' : r'covert video capture (\url{https://www.youtube.com/watch?v=sDzs6y4JVok})',
        r'Policy search and unknown dynamics': r"Implementation of Sergey Levine's work which uses GMMs and linear approximation to estimate robot dynamics using small number of runs of the hardware. It uses estimated dynamics to optimize goal function for black box policy (in my case RNN). Report available online \url{https://www.dropbox.com/s/1e4hm4eidztvxu6/6.867-project.pdf?dl=0}",
    },
    'extra_info': {
        'Research Interests': 'My research concerns applying machine learning techniques for Dialog Systems (think Siri solving more complex problems like planning your day). Specifically I am interested in text generation using modern machine learning techniques (RNNs, NTMs etc.). My academic adviser is Brian Williams.',
        'Research Assistantship': 'My PhD is sponsored by TATA Center at MIT. Part of my research involves traveling to rural areas in India and deploying my algorithms on village scale power microgrid.',
    },
}

dropbox = {
    'fixup': str(0.0),
    'when': 'Fall 2013',
    'role': 'Software Engineering Intern',
    'where': 'Dropbox',
    'image' : 'dropbox.png',
    'description': "I implemented early version of Livefill 2.0 (graph processing system for various jobs on executed on files - thumbnails, pdf previes any many more). My biggest achievement was designing and implementing real-time reserialization of traffic (put messages back in order in which they arrived into the system after some parallel processing). There were also countless little features that were included - automatically created statistics, quick and simple adding of new handlers, automated failure recovery, message aggregation, Redis based queuing system, separation of traffic into scopes (failure in one does not affect others) and of course porting all the traffic from old system to new system. By the time I left all of Dropbox was running it internally and we had large portion of users shadowed. Now it is running 100\% production traffic."
}



dropbox = {
    'fixup': str(0.0),
    'when': 'Fall 2013',
    'role': 'Software Engineering Intern',
    'where': 'Dropbox',
    'image' : 'dropbox.png',
    'description': "I implemented early version of Livefill 2.0 (graph processing system for various jobs on executed on files - thumbnails, pdf previes any many more). My biggest achievement was designing and implementing real-time reserialization of traffic (put messages back in order in which they arrived into the system after some parallel processing). There were also countless little features that were included - automatically created statistics, quick and simple adding of new handlers, automated failure recovery, message aggregation, Redis based queuing system, separation of traffic into scopes (failure in one does not affect others) and of course porting all the traffic from old system to new system. By the time I left all of Dropbox was running it internally and we had large portion of users shadowed. Now it is running 100\% production traffic."
}

google2 = {
    'fixup': str(1.0),
    'when': 'Summer 2012',
    'role': 'Software Engineering Intern',
    'where': 'Google',
    'image' : 'google.png',
    'description': "Adding semantic metrics to Google Analytics.",
}

google1 = {
    'fixup': str(1.0),
    'when': 'Summer 2011',
    'role': 'Software Engineering Intern',
    'where': 'Google',
    'image' : 'google.png',
    'description': "Working on features for Chrome Operating System"
}

cambridge = {
    'when': r'Jul 2010-Oct 2011',
    'where': r'Intech Inc',
    'role': r'Summer Intern',
    'image': 'mit.png',
    'extra_info' : {}
}

events = [mit, dropbox, google2, google1]

# DON'T EDIT BELOW THIS LINE
first_names = ' '.join(name.split(' ')[:-1])
last_name = name.split(' ')[-1].upper()
