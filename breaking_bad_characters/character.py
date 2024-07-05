class Character: 
    def __init__(self, name, phrase, job, action, portrayed_by):
        self.name = name
        self.phrase = phrase
        self.job = job
        self.action = action
        self.portrayed_by = portrayed_by

    def say_name(self, name, phrase):
        return 'My name is {}. {}'.format(self.name, self.phrase)

    def get_info(self):
        return {
            'Name': self.name,
            'Phrase': self.phrase,
            'Occupation': self.job,
            'Action': self.action,
            'Portrayed By': self.portrayed_by
        }