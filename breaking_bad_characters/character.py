'''
    A parent class for Breaking Bad Characters. 

    Parameters: Name, Phrase, Job, Action, Portayed_By 

    Methods: say_name(), get_info()

    '''

class Character: 
    def __init__(self, name, phrase, job, action, description, portrayed_by):
        self.name = name
        self.phrase = phrase
        self.job = job
        self.action = action
        self.description = description
        self.portrayed_by = portrayed_by

    '''
    A method that greets the user, introduces character name,
    and says character catch phrase.

    Args: name, phrase

    return 'My name is {name}. {Phrase}
    
    example: walt.say_name() could output
    "Hello, my name is Walter White. Let's cook."

    '''
    def say_name(self):
        return 'My name is {}. {}'.format(self.name, self.phrase)


    '''
    A method that returns all info about character and displays
    it with labels for readability and improved UX. 

    Args: none

    example return: 
    'Name: Walter White, Phrase: "Everything I do, I do for this family.", 
    Occupation: Chemistry Teacher,
    Portrayed By: Bryan Cranston'
    
    '''
    def get_info(self):
        return {
            'Name': self.name,
            'Phrase': self.phrase,
            'Occupation': self.job,
            'Action': self.action,
            'Description': self.description,
            'Portrayed By': self.portrayed_by
        }
    
    '''
    A method that returns all info about character and displays
    it with labels for readability and improved UX. 

    Args: none

    example return: 
    'Name: Walter White, Phrase: "Let's Cook", 
    Occupation: Methamphetamine Manufacturer,
    Action: Cook, Portrayed By: Bryan Cranston'
    
    '''
    def print_info(self):
        print(f'Name: {self.name}, Phrase: {self.phrase}, Occupation: {self.job}, '
              f'Action: {self.action}, Description: {self.description}, '
              f' Portrayed By: {self.portrayed_by} ')
        
    
class Walt(Character):
    def __init__(self):
        super().__init__(
            name = 'Walter White',
            phrase = 'Everything I do, I do for this family.',
            job = 'Teacher',
            action = 'Cook',
            description = 'An overqualified high school chemistry teacher that' \
            'gets sick with cancer. In an effort to provide for his family, he decides to' \
            'partner with former student, Jesse Pinkman, to produce and sell methamphetamine.',
            portrayed_by = 'Bryan Cranston'
        )
        self.alias = 'Heisenberg'

class Heisenberg(Walt):
    def __init__(self):
        super().__init__()

        self.name = 'Heisenberg'
        self.phrase = 'Say my name.'
        self.job = 'Drug Kingpin'
        self.action = 'Intimidate'
        self.description = 'Initially starting as an alias for Walter White, Heisenberg is' \
            'a ruthless methamphetamine kingpin that will do anything to build his empire. He' \
            'gets what he wants through intimidation, intricate lies, manipulating others, and' \
            'sometimes killing anyone who stands in his way. He represents the egotistical and sociopathic' \
            'side of Walter White.'

class Jesse(Character):
    def __init__(self):
        super().__init__(
            name = 'Jesse Pinkman',
            phrase = 'Yo, yo, yo!',
            job = 'Meth Cook',
            action = 'Making Fat Stacks',
            description = 'A drugee burnout and former student of Walter White. Jesse dabbles in' \
            'drug dealing, but eventually partners with Walter White (Heisenberg) to build a massive' \
            'drug empire.',
            portrayed_by = 'Aaron Paul'
        )

class Skyler(Character):
    def __init__(self):
        super().__init__(
            name = 'Skyler White',
            phrase = 'Do not...sell marijuana to my husband.',
            job = 'Bookkeeper and Author',
            action = 'Being suspicious of Walt',
            description = 'The wife of Walter White and sister of Marie Schrader. Skyler is suspicious of Walter' \
            'early on. She eventually kicks Walt out of the home, worrying that he is putting the family in danger.',
            portrayed_by = 'Anna Gunn'
        )

class Walter_Jr(Character):
    def __init__(self):
        super().__init__(
            name = 'Walter Jr.',
            phrase = 'Something, something, breakfast.',
            job = 'Son',
            action = 'Eat Breakfast',
            description = 'The son of Walter and Skyler White. He likes to eat breakfast' \
            'and is always getting rides to school from Louis.',
            portrayed_by = 'RJ Mitte'
        )
        self.alias = 'Flynn'

class Hank(Character):
    def __init__(self):
        super().__init__(
            name = 'Hank Schrader',
            phrase = 'It\'s easy money...till we catch you!', # FIX ME 
            job = 'DEA Agent',
            action = 'Obsess over Heisenberg',
            description = '',
            portrayed_by = 'Dean Norris'
        )

class Marie(Character):
    def __init__(self):
        super().__init__(
            name = 'Marie Schrader',
            phrase = 'YOU...are in big trouble.',
            job = 'Radiologoy Technician',
            action = 'Steal',
            description = 'The wife of Hank Schrader and sister of Skyler White.' \
            'She enjoys the color purple and stealing things',
            portrayed_by = 'Raymond Cruz'
        )

class Tuco(Character):
    def __init__(self):
        super().__init__(
            name = 'Tuco Salamanca',
            phrase = 'Tight, tight, yeah!',
            job = 'Drug Distributor',
            action = 'Snorting drugs off a bowie knife and beating his homies when they diss him',
            description = 'A sadistic, high-level, drug distributor for the Salamanca cartel',
            portrayed_by = 'Raymond Cruz'
        )