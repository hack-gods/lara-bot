from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot


def init():
    response = str(bot.get_response('oi'))
    response = response.split('$')
    return {'perguntas': response[0], 'resposta': [response[1],response[2]]}
    


def get_user_message(user_text):
    response = str(bot.get_response(user_text))
    response = response.split('$')

    get_response = response[0]
    response.pop(0)

    return  {'perguntas': get_response, 'resposta': response}


bot_name = "Lara"
bot = ChatBot(bot_name)


symptoms = [
    """
    1) Febre alta, tosse seca, cansaço, fadiga, dificuldade para respirar.
    2) Febre, tosse, dor de cabeça, dor nos musculo e nas juntas, dor de garganta.
    3) Espirros, tosse, dor de cabeça, coriza."""
]


phrases = [
    "Olá, sou a Lara uma enfermeira virtual. Vamos começar uma consulta", # 0
    "Você esteve com pessoas que chagaram recentemente de viagem?$sim$não",#1
    """Você está com esses sintomas? (Escolha a opção). 
        1) Febre alta, tosse seca, cansaço, fadiga, dificuldade para respirar
        2) Febre, tosse, dor de cabeça, dor nos musculo e nas juntas, dor de garganta
        3) Espirros, tosse, dor de cabeça, coriza$1$2$3""",# 2
    'É possível que esteja com COVID-19. Procure um médico e fique em isolamento domiciliar$OK', #3
    'É possível que esteja com apenas uma gripe$OK', #4
    'É possivel que esteja com uma alergia$OK', #5
    'Digite "dica" caso Deseje receber dicas de alimentação.$dica', #6
    """Sugerimos comer frutas, alho e cebola, alimentos com ômega 3,evite comer alimentos industrializados e ingerir bebidas alcólicas.
    É de extrema importancia não se esquecer de higienizar as mãos, evite tocar o rosto e cubra a boca com o antebraço ao tossir$oi"""  #7                                                                  
]


conversation = [
    'Oi', f'{phrases[0]}. {phrases[1]}',
    'não', f'{phrases[2]}',
    'sim', f'{phrases[2]}',
    '1', f'{phrases[3]}',
    '2', f"{phrases[4]}",
    '3', f"{phrases[5]}",
    'ok', f"{phrases[6]}",
    'dica', f"{phrases[7]}"
]


trainer = ListTrainer(bot)
trainer.train(conversation)

