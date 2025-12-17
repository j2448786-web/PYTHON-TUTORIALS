print('Welcome to packing helper!')

print('=' * 30)

weather = input('is it sunny?(yes/no): ').lower()

beach_trip = input('are u going to the beach? (yes/no): ').lower()

packing_list = []

if weather == 'yes':
    packing_list.append('t-shirt')
    packing_list.append('short')
    packing_list.append('speaker')
    print('added sunny clothes')
else:
    packing_list.append('jacket and umbrella')
    print('added rainy clothes')
    
if beach_trip == 'yes':
    packing_list.append('swimming costume')
    packing_list.append('sunscreen')
    print('added beach items')
    
packing_list.append('toothbrush')
packing_list.append('towel')
print('added to basic essenitials')

print('=' * 30)
print(f' Your packing List ({len(packing_list)} items:')
print('=' * 30)

for item in packing_list:
    print(f"• {item}")

print("\nHave a great trip! ✈️") 



    
    
    


