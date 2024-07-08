import textwrap

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
    A method that prints all info about character and displays
    it on separate lines with labels for readability and improved UX. 

    Args: none

    example return: 
    'Name: Walter White, Phrase: "Let's Cook", 
    Occupation: Methamphetamine Manufacturer,
    Action: Cook, Portrayed By: Bryan Cranston'
    
    '''
    def print_info(self):
        info = self.get_info()
        for key, value in info.items():
            if key == 'Description':
                # Use textwrap import to wrap text and prevent word break
                wrapped_value = textwrap.fill(value, width=110)
                print(f'{key}: \n{wrapped_value}')
            else:     
                print(f'{key}: {value}')
        
    
class Walt(Character):
    def __init__(self):
        super().__init__(
            name = 'Walter White',
            phrase = 'Everything I do, I do for this family.',
            job = 'Teacher',
            action = 'Cook',
            description = 'An overqualified high school chemistry teacher that' \
            'gets sick with cancer. In an effort to provide for his family, he decides to ' \
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
            description = 'A former student of Walter White and a small-time methamphetamine manufacturer, ' \
            'Jesse Pinkman partners with Walter to produce high-quality methamphetamine. He struggles with ' \
            'addiction and the moral implications of his actions.',
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
            phrase = '** Walter jr. says something about breakfast...**',
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
            phrase = 'It\'s easy money...till we catch you!', 
            job = 'DEA Agent',
            action = 'Obsess over Heisenberg',
            description = 'Walt\'s brother-in-law and a dedicated DEA agent. ' \
            'Hank is committed to fighting the drug trade and is unknowingly pursuing ' \
            'his own brother-in-law in his investigation of the methamphetamine kingpin Heisenberg.',
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

class The_Cousins(Character):
    def __init__(self):
        super().__init__(
            name = 'Marco and Leonel Salamanca',
            phrase = 'No...muy facil.',
            job = 'Cartel Hitmen',
            action = 'Stare menacingly',
            description = 'Twin hitmen working for the Salamanca drug cartel. They are known for their '\
            'silent demeanor and relentless pursuit of their targets.',
            portrayed_by = 'Luis and Daniel Moncada'
        )
        self.fun_fact = 'The actors are not actually twins, but they are related!'

class Gus(Character):
    def __init__(self, status):
        super().__init__(
            name = 'Gus Fring',
            phrase = 'I hide in plain site.',
            job = 'Drug Lord',
            action = 'Run Territory north of border',
            description = 'A highly successful and meticulous drug lord who runs a chain of fast-food ' \
            'restaurants as a front for his methamphetamine distribution network. Gus Fring is known for ' \
            'his calm demeanor and ruthless business tactics.',
            portrayed_by = 'Giancarlo Esposito'
        )
        self.status = status; 

    def set_status(self, status):
        self.status = status
        if status == 'angry':
            self.phrase = 'Don Eladio esta muerto!'

class Saul(Character):
    def __init__(self):
        super().__init__(
            name = 'Saul Goodman',
            phrase = 'Better Call Saul!',
            job = 'Lawyer',
            action = 'Scheme elaborately',
            description = 'A flamboyant and unscrupulous lawyer who represents Walter White and Jesse Pinkman. '\
            'He is adept at bending the law to suit client needs.',
            portrayed_by = 'Bob Odenkirk'
        )
        self.alias = 'Jimmy McGill'

class Mike(Character):
    def __init__(self):
        super().__init__(
            name = 'Mike Ehrmantraut',
            phrase = 'No more half measures',
            job = '"Problem Fixer"',
            action = 'Choke people at Cartel Pool Party.',
            description = 'A former Philadelphia police officer and a fixer for Gus Fring. Mike Ehrmantraut is '\
            'highly skilled in security and enforcement, often handling difficult situations with a calm and methodical approach.',
            portrayed_by = 'Jonathan Banks'
        )

class Badger(Character):
    def __init__(self):
        super().__init__(
            name = 'Badger',
            phrase = 'Darth Vader Had Responsibilities. He Was Responsible For The Death Star.',
            job = 'Drug Dealer',
            action = '**HELICOPTER**',
            description = 'A friend of Jesse, Badger is a well-meaning but often clueless individual '\
            'who frequently gets into trouble.',
            portrayed_by = 'Matt Jones'
        )

class Skinny_Pete(Character):
    def __init__(self):
        super().__init__(
            name = 'Skinny Pete',
            phrase = 'Church, yo.',
            job = 'Drug Dealer',
            action = 'Playing the piano',
            description = 'A friend and associate of Jesse Pinkman, Skinny Pete is a small-time meth dealer. '\
            'He often finds himself caught up in dangerous situations.',
            portrayed_by = 'Charles Baker'
        )
    
class Jane(Character):
    def __init__(self):
        super().__init__(
            name = 'Jane Margolis',
            phrase = 'D-B-A-A',
            job = 'Artist',
            action = 'Draw',
            description = 'Jane Margolis is the girlfriend of Jesse Pinkman and a recovering drug addict. '\
            'She offers Jesse emotional support but ends up introducing him to heroin, which ultimately leads' \
            'to tragic consequences.',
            portrayed_by = 'Krysten Ritter'
        )

class Gomez(Character):
    def __init__(self):
        super().__init__(
            name = 'Steve Gomez',
            phrase = 'Operation Breath Mint.',
            job = 'DEA Agent',
            action = 'Bustin bad guys. DEA Style!',
            description = 'Hank\'s loyal and competent partner at the DEA. He is dedicated to his job '\
            'and supports Hank in his pursuit of the drug trade, often providing crucial insights and backup.',
            portrayed_by = 'Steven Michael Quezada'
        )

class Don_Eladio(Character):
    def __init__(self, fun_fact):
        super().__init__(
            name = 'Don Eladio Veunte',
            phrase = 'Salud.',
            job = 'Drug Kingpin for Salamanca Cartel',
            action = 'Drink poisoned Zafiro Anejo',
            description = 'Don Eladio Vuente is a powerful and ruthless Mexican drug lord who controls the cartel '\
            'that Gus Fring ultimately seeks to overthrow. He commands respect and fear among his associates and rivals.',
            portrayed_by = 'Steven Bauer'
        )
        self.fun_fact = 'Don Eladio is played by Steven Bauer. He portrayed Manny in the film, Scarface. You totally did not realize '\
            'that until I said it!'

class Eliot(Character):
    def __init__(self):
        super().__init__(
            name = 'Eliot Schwartz',
            phrase = 'Yum-Good Ramen?! I thought they outlawed these years ago!',
            job = 'Owners of Gray Matter Technologies',
            action = 'Taking credit for Walt\'s work',
            description = 'Eliot Schwartz is Walt\'s former research partner and co-founder of Gray Matter '\
            'Technologies, a highly successful company in the field of applied sciences. Elliot represents Walt\'s past '\
            'ambitions and serves as a reminder of the professional success that Walter feels he has been denied.',
            portrayed_by = 'Adam Godly'
        )

class Gretchen(Character):
    def __init__(self):
        super().__init__(
            name = 'Gretchen Schwartz',
            phrase = 'If you want to give your kids drug money, do it yourself.',
            job = 'Owners of Gray Matter Technologies',
            action = 'Taking credit for Walt\'s work',
            description = 'Gretchen Schwartz is Eliot\'s wife and Walt\'s former girlfriend. She is also a co-founder '\
            'of Gray Matter Technologies. Gretchen comes from a wealthy background and maintains a strained relationship with Walter '\
            'after their past involvement. She represents a stark contrast to Walt\'s current life and choices.',
            portrayed_by = 'Jessica Hecht'
        )


class Hector(Character):
    def __init__(self):
        super().__init__(
            name = 'Hector Salamanca',
            phrase = '*Ding*',
            job = 'Former drug lord for Salamanca Drug Cartel',
            action = 'Mean mugging everyone',
            description = 'Hector Salamanca is a former high-ranking member of the Salamanca Cartel. He is confined to a wheelchair and '\
            'communicates through a bell due to a stroke (from being poisoned by Gus and Nacho...Better Call Saul spoiler anyone?!). Hector '\
            'has a long history in the drug trade and holds deep animosity towards Gus Fring.',
            portrayed_by = 'Mark Margolis'
        )

## FIX ME 

class Lydia(Character):
    def __init__(self):
        super().__init__(
            name = 'Skinny Pete',
            phrase = 'Church, yo.',
            job = 'Drug Dealer',
            action = 'Playing the piano',
            description = 'A friend and associate of Jesse Pinkman, Skinny Pete is a small-time meth dealer. '\
            'He often finds himself caught up in dangerous situations.',
            portrayed_by = 'Charles Baker'
        )

class Todd(Character):
    def __init__(self):
        super().__init__(
            name = 'Skinny Pete',
            phrase = 'Church, yo.',
            job = 'Drug Dealer',
            action = 'Playing the piano',
            description = 'A friend and associate of Jesse Pinkman, Skinny Pete is a small-time meth dealer. '\
            'He often finds himself caught up in dangerous situations.',
            portrayed_by = 'Charles Baker'
        )

class Uncle_Jack(Character):
    def __init__(self):
        super().__init__(
            name = 'Skinny Pete',
            phrase = 'Church, yo.',
            job = 'Drug Dealer',
            action = 'Playing the piano',
            description = 'A friend and associate of Jesse Pinkman, Skinny Pete is a small-time meth dealer. '\
            'He often finds himself caught up in dangerous situations.',
            portrayed_by = 'Charles Baker'
        )

class Gale(Character):
    def __init__(self):
        super().__init__(
            name = 'Skinny Pete',
            phrase = 'Church, yo.',
            job = 'Drug Dealer',
            action = 'Playing the piano',
            description = 'A friend and associate of Jesse Pinkman, Skinny Pete is a small-time meth dealer. '\
            'He often finds himself caught up in dangerous situations.',
            portrayed_by = 'Charles Baker'
        )

class Vacuum_Guy(Character):
    def __init__(self):
        super().__init__(
            name = 'Skinny Pete',
            phrase = 'Church, yo.',
            job = 'Drug Dealer',
            action = 'Playing the piano',
            description = 'A friend and associate of Jesse Pinkman, Skinny Pete is a small-time meth dealer. '\
            'He often finds himself caught up in dangerous situations.',
            portrayed_by = 'Charles Baker'
        )