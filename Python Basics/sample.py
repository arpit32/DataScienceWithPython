attribute_names = ['class',
                   'cap-shape', 'cap-surface', 'cap-color',
                   'bruises?',
                   'odor',
                   'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
                   'stalk-shape', 'stalk-root',
                   'stalk-surface-above-ring', 'stalk-surface-below-ring',
                   'stalk-color-above-ring', 'stalk-color-below-ring',
                   'veil-type', 'veil-color',
                   'ring-number', 'ring-type',
                   'spore-print-color',
                   'population',
                   'habitat']

single_instance_str='p,k,f,n,f,n,f,c,n,w,e,?,k,y,w,n,p,w,o,e,w,v,d'

single_instance_list=single_instance_str.split(',')

def attribute_value(instance, attribute, attribute_names):
    '''Returns the value of attribute in instance, based on its position in attribute_names'''
    if attribute not in attribute_names:
        return None
    else:
        i = attribute_names.index(attribute)
        return instance[i]  # using the parameter name here

print('Values for the', len(attribute_names), 'attributes:', end='\n\n')  # adds a blank line
for i in range(len(attribute_names)):
    print(attribute_names[i], '=',
          attribute_value(single_instance_list, attribute_names[i], attribute_names))

