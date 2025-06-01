class QuestFailedException(Exception):
    '''Exception raised when quest fails'''



def complete_quest(success):
    if success:
        print('Congrats')
    else:
        raise QuestFailedException('Quest Failed!')
    
# Main
try:
    quest_outcome= input('Did you complete quest? (y/n)').strip().lower()
    if quest_outcome== 'y':
        complete_quest(True)
    else:
        complete_quest(False)
except QuestFailedException as err:
    print(err)