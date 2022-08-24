
rus = [] 
eng = []

def open_source(origin:str)->list:
    # takes the path to the original file
    with open(origin) as t:
        text = t.read().split('\n')
        return text




def transformation_origin(text:list) -> None:
    '''
     fills arrays in turn where each word on the left side 
     corresponds to all possible translations on the right side
    '''
    for line in text:
        lst_line = line.split('\t') # split line on tab character (\t)
        eng_part_of_line = lst_line[0].split(';')
        rus_part_of_line = lst_line[-1].split(';') # split line on semicolon 
        if len(eng_part_of_line) == 1 and len(rus_part_of_line) == 1:
            '''
            check the string for the length of the elements 
            if the length does not exceed 1 element, 
            then we save it to the result lists without changes
            '''
            eng.append(eng_part_of_line[0]+"\n")
            rus.append(rus_part_of_line[0]+"\n")
        else: 
            '''
            if the number of words in the subarray exceeds 1 element, 
            then we iterate each element of eng_part_of_line 
            with all translation options in rus_part_of_line
            '''
            for i in eng_part_of_line:
                for e in rus_part_of_line:
                    eng.append(i.strip()+"\n")
                    rus.append(e.strip()+"\n")




def record_data(lst1:list,lst2:list) -> None:
    # saving the result of the conversion
    with open("eng.txt", "w") as e:
        e.writelines(lst1)

    with open("rus.txt", "w") as r:
        r.writelines(lst2)




def main(row_text:str):
    # function initialization and creation of final result-files(eng.txt,rus.txt)
        import_txt_for_translate = open_source(row_text)
        transform_into_two_array = transformation_origin(import_txt_for_translate)
        record_translation_result = record_data(eng, rus)
    

 

if __name__ == "__main__":
    # sure that file was run directly, and not imported
    txt_for_translate = "text.txt" # select the text file you want to convert
    try:
        main(txt_for_translate)
        print(f'The script completed!'
              f'\neng.txt and rus.txt were successfully created in the root folder')
    except Exception as error:
        print(error,'\nPlease, make sure the file is in the correct format')
