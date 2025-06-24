from stats import count_words
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]

    with open(path) as f:
        file_contents = f.read()

    number_of_words = count_words(file_contents)

    print(f'''
--- Begin report of {path} ---
{number_of_words} words found in the document
    '''
    )

    format_dict(file_contents)

    print('''--- End report ---
    ''')

def count_letters(text):

    stat_dict = {}

    lowered_text = text.lower()

    for c in lowered_text:
        if c.isalpha():
            try:
                stat_dict[c]+=1
            except:
                stat_dict[c]=1
    
    return stat_dict    

def format_dict(dict):

    res = [{"letter": key, "value": value} for key, value in count_letters(dict).items()]

    res.sort(reverse=True, key=sort_on)

    for item in res:
        letter = item["letter"]
        value = item["value"]
        print(f"{letter}: {value}")

def sort_on(dict):
    return dict["value"]

main()