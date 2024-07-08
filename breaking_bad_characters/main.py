from character import *

walt = Walt()

print("\n")
print(f'Walter White Introduces Himself: "{walt.say_name()}"')
print('\n')
print("Info about Walt: ")
walt.print_info()

print("\n")

bad_walt = Heisenberg()
print(f'**Walt put on his hat. He is now a bad guy.**\n')
print(f'Heisenberg introduces himself: "{bad_walt.say_name()}"')
print('\n')
print("Info about Heisenberg: ")
bad_walt.print_info()

print('\n')

gus = Gus('chillin')
print(f'Gus introduces himself: "{gus.say_name()}"')

gus.set_status('angry')

print('\n')
print('**Gus is angry**')
print('\n')
print(f'Gus yells: {gus.phrase}')
print('\n')