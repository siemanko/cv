# KEEP SCROLLING
from collections import namedtuple

# EDIT HERE

name='Szymon SIDOR'

email='szymon.sidor@gmail.com'
phone='+14438799664'
facebook=r'fb.com/szymon.sidor'

mit = {
    'fixup': str(4.0),
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
        r'Android Security' : r'Covert video capture. Demo available at \url{https://www.youtube.com/watch?v=sDzs6y4JVok}.',
        r'Policy search and unknown dynamics': r"Implementation of Sergey Levine's work which uses GMMs and linear approximation to estimate robot dynamics using small number of runs of the hardware. It uses estimated dynamics to optimize goal function for black box policy (in my case RNN). Report available online \url{https://www.dropbox.com/s/1e4hm4eidztvxu6/6.867-project.pdf?dl=0}.",
        r'Dali' : r'Coauthored deep learning/symbolic differentiation system written in C++. Hogwild enabled. Demonstrated capability to learn simple language models, improved on facebook Toy AI problems LSTM baseline and more. Work in progress. \url{https://github.com/jonathanraiman/recurrentjs}'
    },
    'extra_info': {
        'Research Interests': 'My research concerns applying machine learning techniques for Dialog Systems (e.g. Siri-style assistant solving complex problems like planning your day). Specifically I am interested in text generation using modern machine learning techniques (RNNs, NTMs etc.). My academic adviser is Brian Williams.',
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
    'description': "Worked on features for Chrome Operating System. Implemented flash media formatting, unformatted media detection, screen saver, alternative login methods (OpenID). Investigated potential memory allocation improvements."
}

cambridge = {
    'fixup': str(2.2),
    'when': r'October 2010 - June 2013',
    'where': r'University of Cambridge',
    'role': r'Computer Science Tripos',
    'image': 'cambridge.png',
    'courses': [
       'Concurrent and Distributed Systems',
       'Discrete Mathematics',
       'Digital Signal Processing',
       'Operating Systems',
       'Hoare Logic and Formal Proofs',
       'Compiler Optimization',
       'Natural Language Processing',
    ],
    'competitions': [
        'Facebook Hacker Cup 2013 (210th place)',
        'ACM ICPC qualification round NWERC 2011 (Bronze medal)',
        'VK cup 2012 (193th place)',
    ], 'extra_info': {
        'Overall grades': 'First, second and third year respectively: 1, 1, 2.1',
        'Final year project': r'Springboard - cryptographically secure distributed social network over opportunistic communication supervised by prof. Jon Crowcroft. Report available online \url{https://www.dropbox.com/s/wu9e9jzuvb97die/dissertation-final.pdf?dl=0}',
        'Cambridge Algorithms Society': 'I was the founding member of CAS - the mission was to introduce students to programming competitions. We were also in charge of organizing university-level qualifications for ICPC.'
    }
}

highschool = {
    'fixup': str(1.0),
    'when': r'September 2007 - June 2010',
    'where': r'III Highschool in Gdynia, Poland',
    'role': r'Student',
    'image': '3lo.png',
    'competitions': [
        'Polish Olympiad in Computer Science (25th place)',
        'TopCoder Yellow',
        r'ACM ICPC qualifications CEPC 2009 (1/8 highschools, 20/80 highschools + universities)',
        'Polish Olympiad in Mathematics (twice honorable mentioned)',
    ],
    'description': r"During highschool I sent two months every year at computer science camps organized by Stowarzyszenie Talent. I contributed problems, gave talks and in general helped organize those events."
}

life = {
    'fixup': str(1.0),
    'when': r'30 January 1991 - Current',
    'where': r'Poland, UK, USA and sometimes other places',
    'role': r'Life',
    'image': 'life.jpg',
    'extra_info': {
        'Hobbies': r"Programming Competitions, Sailing, Snowboarding, Martial Arts, Parkour (\url{http://goo.gl/rz3a9}), board games and reading books",
        'My blog': r'\url{http://snacksforyourmind.blogspot.com}',
        'Languages': r"English (fluent), Polish (native), Spanish (experimenting with Duolingo)"
    }
}

events = [mit, dropbox, google2, google1, cambridge, highschool, life]

# DON'T EDIT BELOW THIS LINE
first_names = ' '.join(name.split(' ')[:-1])
last_name = name.split(' ')[-1].upper()

href_email = r'\href{mailto:%s}{%s}' % (email, email)
href_facebook = r'\url{%s}' % (facebook,)
