import wikipedia

def main():
    language = input("Выберите язык для статей в Википедии: (en, fr, ru)")
    wiki = wikipedia
    wiki.set_lang(language)
    while True:
        query = input("Что вам найти в Википедии")
        results = wiki.search(query)
        print()
        for key, for_result in enumerate(results):
            print(key,for_result)
        print()
        about = input("Выберите о чем вам  найти краткую информацию \n")
        summary = wiki.summary(about)
        d = 0
        for i  in range(0,len(summary),30):
            try:
                print(summary[d:d+i],"-")
            except Exception:
                print(summary[d:])
            d += i

        ask_url = input("Вы хотите ли ссылку на статью в Википедии?")
        if ask_url.lower() == "да":
            article = wiki.page(about)
            print(article.url)
main()
