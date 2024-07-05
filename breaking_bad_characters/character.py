'''
    A parent class for Breaking Bad Characters. 

    Parameters: Name, Phrase, Job, Action, Portayed_By 

    Methods: say_name(), get_info()

    '''

class Character: 
    def __init__(self, name, phrase, job, action, portrayed_by):
        self.name = name
        self.phrase = phrase
        self.job = job
        self.action = action
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
              f'Action: {self.action}, Portrayed By: {self.portrayed_by} ')
        
    
class Walt(Character):
    def __init__(self):
        super().__init__(
            name = 'Walter White',
            phrase = 'Everything I do, I do for this family.',
            job = 'Teacher',
            action = 'Cook',
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
    