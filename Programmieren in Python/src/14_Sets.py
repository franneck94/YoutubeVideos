# Sets (Mengen)

familie_mutter = {'angelika', 'petra', 'horst'}
familie_vater = {'dieter', 'anne', 'lothar', 'horst'}

print('dieter' in familie_mutter)
print('dieter' in familie_vater)

familie = familie_mutter | familie_vater
print(familie)

namens_test = familie_mutter & familie_vater
print(namens_test)

namens_test2 = familie_mutter - familie_vater
print(namens_test2)

namens_test3 = familie_mutter ^ familie_vater
print(namens_test3)

familie2 = {person for person in familie_mutter + familie_vater}
print(familie2)
