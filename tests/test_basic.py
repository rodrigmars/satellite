from land_mining import message_mining, InvalidMessageError


def test_repository_add_occurrences():

    message_content = "Lorem ipsum dolor sit amet. Et ipsam aliquam At http://www.maquinadeaposta.com/pixfacil repellat aliquam et voluptatem nulla qui \
        eligendi facilis est consequatur chilly-headline.name,well-to-do-caffeine.net,impartial-start.biz itaque. Et totam quasi et nobis saepe qui perferendis odio\
            non internos ducimus et https://www.linkteste01.com/pt/gerador-de-texto galisum ipsa! Quo unde voluptatem cum deleniti vitae et asperiores quae. \
                Est nulla sapiente ea voluptatum quos et beatae obcaecati eos corrupti nobis et doloremque quae qui \
                    consequatur enim.Ethttps://www.dindinfacil.com/mandapix laudantium quam sed alias http://www.seudinheiroaqui.com/jogo1 luptatem minus sit velit delectus in sint vero. \
                        Nam doloreconsequaturhttp://urlteste02.com/questions ut provident galisum et deserunt dolorem. Et assumenda optio ut distinctio \
                            galisum vel nihil omnis eum dolorum quos aut maiores voluptas cum pariatur esse sit nostrum eveniet!Est fugiat excepturi aut \
                                eligendi molestias in sapientehttp://casadeapostas.com/pixvoluptatem est consequatur libero et dolorem explicabo. Est autem commodi ut nemo modi et \
                                    quia http://www.sejaumapostador.com/apostas consequatur non dignissimos ipsa aut provident \
        molestias qui galisum modi qui illum"

    message_content = "https://www.youtube.com/watch?v=teste123"

    message_content = "[youtube.com](https://www.youtube.com/watch?v=teste123)"

    try:

        message_mining(message_content)()

    except InvalidMessageError as ex:

        print(f"Ação inválida: {ex.message}")

    assert session.query(model.OrderLine).all() == expected
