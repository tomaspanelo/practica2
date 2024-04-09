def es_heterograma(text):
    text= text.lower()
    characters= set()
    for char in text:
        print(char)
        if char.isalpha():
            if char in characters:
                return False
            characters.add(char)
    return True