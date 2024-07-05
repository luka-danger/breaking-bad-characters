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
    def say_name(self, name, phrase):
        return 'My name is {}. {}'.format(self.name, self.phrase)


    '''
    A method that returns all info about character and displays
    it with labels for readability and improved UX. 

    Args: none

    example return: 
    'Name: Walter White, Phrase: "Let's Cook", 
    Occupation: Methamphetamine Manufacturer,
    Action: Cook, Portrayed By: Bryan Cranston'
    
    '''
    def get_info(self):
        return {
            'Name': self.name,
            'Phrase': self.phrase,
            'Occupation': self.job,
            'Action': self.action,
            'Portrayed By': self.portrayed_by
        }