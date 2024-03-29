from flask import Flask
from random import choice

app = Flask(__name__)


def generate_HNY_text():
    # secure_random = random.SystemRandom()
    b = '<br>'
    s1 = choice(['Дорогой', "Милый", 'Драгоценный мой', 'Уважаемый'])
    # Этот год был
    s2 = choice(['не простым', 'не из лёгких', 'неоднозначным', 'противоречивым', 'словно испытание',
                 'полон проблем', 'проблемным'])
    s3 = choice(['одновременно', 'вместе с тем', 'также', 'в то же время'])
    s4 = choice(['ярким на события', 'насыщенным', 'радостным', 'полным эмоций',
                 'запоминающимся', 'непохожим на другие', 'не лишенным радостей'])
    s5 = choice(['И я ценю твой вклад в это', 'И это не без твоей помощи',
                 'И ты помог(ла) этому осуществиться', 'И только благодаря твоей поддержке, я справился(лась)'])

    s6 = choice(['От всей души', 'От всего сердца', 'Искренне', 'Затая дыхание',
                 'С надеждой на будущее', 'С любовью в сердце', 'Сердечно'])
    # Пусть
    s7 = choice(['у тебя все будет так, как ты захочешь', 'будет меньше грусти и забот и побольше радости',
                 'все твои мечты сбудутся', 'подарки сыпятся как из Рога изобилия', 'все планы реализуются',
                 'тебе всегда сопутствует удача', 'радость наполнит каждый твой день',
                 'улыбки будут чаще, а грусть останется в прошлом',
                 'все неприятности останутся в прошлом', 'плохое забудется, а хорошее приумножится'])
    # Желаю тебе, чтобы
    s8 = choice(['тебе всегда сопутствовала удача', 'вдохновение не покидало тебя',
                 'тебе удалось воплотить всё задуманное', 'о тебе слагали легенды', 'год принёс лишь радости',
                 'радостные дни сменялись ещё более радостными', 'реалии соответствовали ожиданиям',
                 'все твои родные были здоровы', 'ты никогда не болел(а)',
                 'здоровье было крепким и денег было достаточно', 'трудности тебя обходили стороной',
                 'в сердце не было зимы', 'в сердце была весна', 'в сердце было лето',
                 'было меньше дней холодных, злых людей',
                 'аромат мандаринов ещё долго сохранял атмосферу праздника',
                 'всё, что мы отдали, вернулось нам втройне'])
    # а новый год стал самым
    s9 = choice(['запоминающимся', 'ярким', 'удачным', 'добрым', 'денежным', 'тёплым',
                 'счастливым', 'прекрасным', 'изумительным', 'тёплым', 'красочным', 'самым', 'лучшим', 'сочным',
                 'сытным', 'душевным', 'волшебным', 'сказочным', 'успешным'])

    congrat = '<html><body><div width="800px">'
    congrat += s1 + '(ая) ИМЯ ДРУГА!' + b
    congrat += 'Этот год был ' + s2 + ', но ' + s3 + ' он был и ' + s4 + '. ' + s5 + '!' + b
    congrat += s6 + ' поздравляю тебя с праздником!' + b + 'Пусть ' + s7 + '! Желаю тебе, чтобы ' + s8 + ', а новый год стал самым ' + s9 + '!' + b
    congrat += 'С новым счастьем!'
    congrat += '<//div><//body><//html>'

    return congrat


def generate_8_of_march_text(official=False):
    you = ('ты', "тебя") if not official else ("Вы", "Вас")
    v1 = ['8-ым марта',
          'главным праздником весны',
          'Международным женским днём']
    from_the_bottom_of_my_heart = ['От всего сердца',
                                   "От всей души",
                                   "От души",
                                   "От самого сердца",
                                   "От чистого сердца",
                                   "С открытой душой",
                                   ]

    text = f'''{choice(from_the_bottom_of_my_heart)} поздравляю {you[1]} с {choice(v1)}!<br />
    Этот замечательный праздник наполнен особой радостью и теплотой.
    Сегодня мы говорим спасибо мамам – за жизнь, которую вы нам подарили.
    Женам и дочерям – за счастье быть мужем и отцом.
    Женщинам-коллегам – за поддержку и понимание.
    Вы наполняете нашу жизнь особым смыслом, делаете ее ярче.
    Ваша любовь помогает нам выстоять во времена тяжелых испытаний.
    В современном мире вы добиваетесь больших профессиональных успехов.
    Ярко проявляете себя на ответственной работе, в предпринимательстве и творчестве, в общественной и культурной жизни.
    Вы успеваете все и при этом остаетесь нежными и заботливыми хранительницами домашнего уюта и тепла.
    Вы всегда будете занимать главное место в нашей жизни и в наших сердцах.
Пусть сегодня и всегда вас окружают забота и любовь. Счастья вам, радости и добра, дорогие наши, любимые женщины!'''

    return '<html><body><div width="800px">'+text+'<//div><//body><//html>'


@app.route('/')
def index():
    return generate_8_of_march_text()


if __name__ == '__main__':
    app.run()
