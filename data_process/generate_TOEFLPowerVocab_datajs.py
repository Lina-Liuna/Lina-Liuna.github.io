import sys
sys.path.append('/Users/linaliu/code/EnglishSkills/')

from english_skills_books import TOEFLPowerVocab as TOEFL_voc

import random


def get_words_dict_list():
    voc_dict = {}
    for dict in  TOEFL_voc.words_list:
        voc_dict.update(dict)
    return voc_dict




def get_random_item(vocdicts):
    # Get a random key from the dictionary
    random_key = random.choice(list(vocdicts.keys()))

    # Access the corresponding value using the random key
    random_words_meaning = vocdicts[random_key].replace('"', '')

    return random_words_meaning



def generate_question_str( key, value, vocdicts, question_no):
    optionlist = []
    value = value.replace('"', '')
    optionlist.append(value)
    optionlist.append(get_random_item(vocdicts))
    optionlist.append(get_random_item(vocdicts))
    optionlist.append(get_random_item(vocdicts))
    random_number = random.randint(0, 3)
    qstr = f"    {{\n    numb: {question_no},\n    question: \"{key}\",\n    answer: \"{value}\",\n    options: [\n      \"{optionlist[random_number]}\",\n"

    optionlist.remove(optionlist[random_number])
    random_number = random.randint(0,2)
    qstr += "      \"" + optionlist[random_number] + "\",\n"
    optionlist.remove(optionlist[random_number])
    random_number = random.randint(0,1)
    qstr += "      \"" + optionlist[random_number] + "\",\n"
    optionlist.remove(optionlist[random_number])
    qstr += "      \"" + optionlist[0]  + "\",\n    ]\n  },\n"

    return qstr

def generate_all_strs(vocdicts ):
    voc_strs = "\n\nlet questions = [\n"
    for index, (key, value) in enumerate(vocdicts.items(), start=1):

        voc_strs += generate_question_str( key, value, vocdicts, index)
    voc_strs += "];\n"
    return voc_strs

def all_strs2file(strs, file_path):
    with open(file_path, 'w') as file:
        file.write(strs)

sevendays_voc_list = get_words_dict_list()
print(sevendays_voc_list)
words_strs = generate_all_strs(sevendays_voc_list)

filepath = "/Users/linaliu/code/Lina-Liuna.github.io/js/linked_TOEFL_Power_Vocab.js"
all_strs2file(words_strs, filepath)





