from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot


def first_lara_message():
    response = str(bot.get_response('oi'))
    response = response.split('$')
    return {'perguntas': response[0], 'resposta': [response[1],response[2]]}    


def get_user_message(user_text):
    response = str(bot.get_response(user_text))
    response = response.split('$')

    get_response = response[0]
    response.pop(0)

    return  {'perguntas': get_response, 'resposta': response}


phrases = [
        """Olá eu sou a Lara, vou te fazer algumas perguntas ok?
        1)sim :) 
        2)não obrigado :/
        $1[0]$2[0]""",

        "Você esteve em contado com pessoas que chegaram recentemente de viagem?$sim[1]$não[2]",

        """Neste momento o senhor(a) apresenta alguns destes sintomas?
        1) Febre, cansaço
        2) Febre,cansaço, dor de cabeça, dor no corpo mal-estar, tosse seca
        3) Nenhuma das alternativas.$1[1]$2[1]$3[1]""",

        """Os sintomas indicam um quadro no qual deve-se ser avaliado por um médico o quanto antes,
           caso tenha bastante dificuldade de respirar procure um hospital.
           Lembre-se também de NÃO realizar a automedicação, pois esta prática pode agravar seu quadro clínico, evite sempre aglomerações.""",

        """Fique atento se você possui alguma doença crônica, pois o quadro clínico pode se agravar com a infecção por COVID-19.
           Continue em isolamento social, prevenindo-se e ajudando a não contaminar, mantenha hábitos saudáveis."""                                                   
]


conversation = [
    'Oi', f'{phrases[0]}',
    '1[0]', f'{phrases[1]}',
    '2[0]', f'{phrases[1]}',
    'sim[1]', f'{phrases[2]}',
    'não[1]', f"{phrases[2]}",
    '1[2]', f"{phrases[4]}",
    '2[2]', f"{phrases[3]}",
    '3[2]', f"{phrases[4]}",
]


bot_name = "Lara"
bot = ChatBot(bot_name)


trainer = ListTrainer(bot)
trainer.train(conversation)

