from flashtext import KeywordProcessor

string = 'hello from Jamaica! I need grapes'

keyword_processor = KeywordProcessor()
keyword_processor.add_keyword('Jamaica', 'J Town')

new_sentence = keyword_processor.replace_keywords(string)
print(new_sentence)