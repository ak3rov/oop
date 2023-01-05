designations = []
codes = []
data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
for i in data:
    if i.isnumeric():
        codes.append(i)
    else:
        designations.append(i)
i = 0
operators = dict()

while i < len(codes):
    operators[designations[i]] = {codes[i]}
    i += 1

del operators['Fonex']
del operators['Katel']

operators['O!'].add('0700')
operators['O!'].add('0500')
operators['Megacom'].add('0555')
operators['Megacom'].add('0999')
operators['Beeline'].add('0222')
operators['Beeline'].add('0777')

for i, v in operators.items():
    print(f'{i} - {v}')