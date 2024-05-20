from utils import get_words, check_url


def message_mining(message):

    domains = ["https://www.youtube.com/",
               "https://stackoverflow.com/",
               "https://stackoverflow.blog/",
               "https://github.com/",
               "https://www.geeksforgeeks.org/",
               "https://www.python.org/",
               "https://nodejs.org/en",
               "https://developer.mozilla.org/",
               "https://www.javascripttutorial.net/",
               "https://dev.java/",
               "https://dev.to/",
               "https://medium.com/"]

    def check_domain(url: str) -> bool:
        return False if url not in domains else True

    def valid_message():

        for word in get_words(message):

            if check_url(word):

                if not check_domain(word):

                    print(
                        "Mensagem contendo endereço de URL nao permitido.")

                    break

    return valid_message
