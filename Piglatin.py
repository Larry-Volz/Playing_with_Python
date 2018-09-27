#PIGLATIN TRANSLATOR

""" User can type in a phrase and this will parse that phrase and print
it back to them in piglatin"""

phrase = ''
for ii in range(50):
    print('')

print("Doc Volz's Piglatin Translator")


    

def translate_to_piglatin(phrase):
        for ii in range(4):
            print('')
    
        print('Translation:')
        word_list = phrase.split(" ")  #breaks phrase into list variable
        phrase =''
        for index in range(len(word_list)): #for each word in list
            individual_word = word_list[index]  #separate word to work with
            first_letter=individual_word[0]   #separate the 1st letter
            rest_=individual_word[1:]        #separate the rest
            piglatin_translation = rest_ + first_letter + 'ay '  #convert
          
            phrase = phrase + piglatin_translation  #add it to final phrase
            
        return phrase       #return the result of all the hard work


while phrase !='e':
        for ii in range(4):#variable ii is better than i because more searchable
            print('')
        print("Type in what you want translated or 'e' to end")
        phrase = input('> ')

        if phrase == 'e':
            break
        else:
            final_translation = translate_to_piglatin(phrase)
            print(final_translation)


