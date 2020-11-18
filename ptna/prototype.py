from ptna_ptna import Ptna,Emotion
def prompt(obj):
    """
    docstring
    """
    return obj.gat_name() + obj.get_responder_name() + '>'
print ('Ptna System prototype : ptna')
ptna = Ptna('ptna')
while True:
    inputs = input('>')
    if not inputs:
        print('ばいばい')
        break
    response = ptna.dialogue(inputs)
    print(prompt(ptna),response)
        