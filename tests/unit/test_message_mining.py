import pytest
from bot.utils import get_all_links
from exceptions.custom_errors import InvalidMessageError, Invalid

from bot.land_mining import message_mining

# @pytest.mark.skip(reason="")


def test_check_total_three_links():

    message_content = "non internosducimusethttps://www.maquinetadasorte.com/pt/gerador-de-texto galisum ipsa! https://www.jogatinadameianoite.com/ Quo unde voluptatem cum https://www.jogodoazarao.com/ voluptatem  voluptatem"

    result = list(filter(lambda x: x in ["https://www.maquinetadasorte.com/pt/gerador-de-texto",
                                         "https://www.jogatinadameianoite.com/", "https://www.jogodoazarao.com/"], get_all_links(message_content)))

    assert len(result) == 3


def test_raises_exception():
    with pytest.raises(InvalidMessageError):
        raise InvalidMessageError(Invalid.LINK, 'Web link nao permitido!')


def test_raises_exception_web_link():

    message_content = "[www.linkteste01.com] (https://www.linkteste01.com/pt/gerador-de-texto)"
    web_link = "https://www.linkteste01.com/pt/gerador-de-texto"

    with pytest.raises(InvalidMessageError) as exc_info:

        message_mining(message_content)()

    assert exc_info.value.args[1] == f"Web link '{web_link}' nao permitido!"


def test_raises_exception_web_link_with_text():

    message_content = "non internosducimusethttps://www.linkteste01.com/pt/gerador-de-texto galisum ipsa! Quo unde voluptatem cum"
    web_link = "https://www.linkteste01.com/pt/gerador-de-texto"

    with pytest.raises(InvalidMessageError) as exc_info:

        message_mining(message_content)()

    assert exc_info.value.args[1] == f"Web link '{web_link}' nao permitido!"


def test_raises_exception_multiple_web_links():

    message_content = "Lorem ipsum dolor sit amet. Et ipsam aliquam At https://www.dindinfacil.com/mandapix http://casadeapostas.com/pixvoluptatem"
    web_link = "https://www.dindinfacil.com/mandapix"

    with pytest.raises(InvalidMessageError) as exc_info:

        message_mining(message_content)()

    assert exc_info.value.args[1] == f"Web link '{web_link}' nao permitido!"
