SELECT word, occurances
FROM word_rank
where word not in (
    'a', 'to', 'this', "I'm", "don't", 'can', "that's", 'not', 'here', 'on', 'my', 'I', 'the', 'me', 'all', 'it', 'that', 'is', 'and', 'we', 'in',
    'get', 'have', 'so', 'just', 'of', 'like', 'be', 'for', 'but', 'know', 'you', 'with', 'now', "it's", 'do', 'good', 'if', 'one', 'as', 'what', 'little',
    'room', 'go', 'will', 'up', 'our', 'there', 'really', 'us', 'was', 'think', 'out', 'are', 'gonna', 'at', 'got', "we're", 'then', 'more', 'could', 'use',
    'want', 'still', 'even', 'which', 'well', 'right', 'take', 'ok', 'going', 'probably', 'pretty', 'should', 'maybe', 'also', 'way', 'would', 'about', 'or',
    'much',' they', 'some', 'see', 'these', 'by', 'might', 'run', 'make', 'time', 'they', 'enough', 'from', 'an', 'because', 'bit', 'something', 'mean', 'your',
    'very', 'great', 'next', 'did', 'say', 'been', 'into', 'how', 'them', 'give', 'better', 'least', 'too', 'where', 'man', 'try', "there's", "you're", 'than',
    'guess', 'bad', 'kind', 'hard',' when', 'his', 'gotta', "let's", 'doing', "didn't", 'had', 'getting', 'he', 'i', 'pick', 'sure', 'lot', "doesn't", 'those',
    'sprint', 'their', 'two', 'done', 'any', 'only', 'through', 'were', 'first', 'may', 'point', 'long', 'second', "we'll", 'another', 'every', 'other', 'far',
    'feel', 'again', 'find', 'though', 'able', 'course', "I'd", "we've", 'being', 'never', 'extra', "I'll", 'come', 'end', 'already', 'fine', 'its', 'keep', 'start',
    'instread', 'before', 'game', 'does', 'has', "they're", 'work', 'said', 'anything', 'people', 'after', 'black', 'kill', 'nice', 'things', 'new', 'yet', 'own',
    'thing', 'things', 'seems', "he's", "can't", 'put', 'always', 'taking', 'red', 'away', 'three', 'idea', 'year', 'look', 'almost', 'stuff', 'double', 'nothing',
    'real', 'gives', 'off', 'many', 'live', 'happen', 'super', 'easy', 'last', 'makes', 'oh', 'runs', 'looking', 'big', 'care', 'play', 'ever', 'him', 'myself', 'goes'
)
order by occurances desc
;
