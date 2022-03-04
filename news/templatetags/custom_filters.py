from django import template

register = template.Library()


@register.filter(name='censor')
def censor(text):
    bad_words = ['badword1', 'badword2']
    new_text = text.split(' ')
    for i, word in enumerate(new_text):
        for bad_word in bad_words:
            if word == bad_word:
                new_text[i] = (new_text[i][0]+'*'*(len(word)-2)+new_text[i][-1])
    censored = ' '.join(new_text)
    return censored
