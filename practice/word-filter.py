# coding:utf-8
def text_create(name, msg):
    desktop_path = 'D:/用户文件/09403/桌面/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done')


def text_filter(word, censored_word='lame', changed_word='Awesome'):
    return word.replace(censored_word, changed_word)


def censored_text_create(name, msg):
    clean_msg = text_filter(msg)
    text_create(name, clean_msg)


censored_text_create('test', 'lame!lame!lame!')

