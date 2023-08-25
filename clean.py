import re

def removeWhitespace(text):
    """ removes whitespace from the beginning and ending of each line
    """
    pattern = r'^\s+|r\s+$'   
    result = re.sub(pattern, '', text)
    return result

def removeSpeakerName(text):
    """ removes names in capital followed by a '.' at the beginning of each line 
        and all the Words in capital
    """
    pattern=r'\b[A-Z][A-Z]+\.|\b[A-Z]+\b'
    result=re.sub(pattern,'', text) 
    return result

def removeLinesBasedOnWords(words,text):
    """Removes a line based on the words provided in a list
    """
    if len(words) > 0:
        pattern = '|'.join(r'\b{}\b'.format(re.escape(word)) for word in words)
        pattern = r'^.*(?:' + pattern + r').*$'
        result = re.sub(pattern, '', text)
        return result
    else:
        print('Please provide a list with words')

def removeWords(words,text):
    """Removes words from a line provided in a list
    """
    if len(words) > 0:
        pattern = '|'.join(r'\b{}\b'.format(re.escape(word))for word in words) 
        result = re.sub(pattern, '', text)
        return result
    else:
        print('Please provide a list with words')

def remove_words_in_brackets(text):
    """Removes words in brackets (including the brackets)
    """
    pattern = r'\[.+?\]|\(.+?\)'
    result = re.sub(pattern, '', text)
    return result