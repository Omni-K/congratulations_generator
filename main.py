from flask import Flask
import random

app = Flask(__name__)


def generate_text():
    #secure_random = random.SystemRandom()
    b = '<br>'
    s1 = random.choice(['Дорогой', "Милый", 'Драгоценный мой', 'Уважаемый'])
    # Этот год был
    s2 = random.choice(['не простым', 'не из лёгких', 'неоднозначным', 'противоречивым', 'словно испытание',
                        'полон проблем', 'проблемным'])
    s3 = random.choice(['одновременно', 'вместе с тем', 'также', 'в то же время'])
    s4 = random.choice(['ярким на события', 'насыщенным', 'радостным', 'полным эмоций',
                        'запоминающимся', 'непохожим на другие', 'не лишенным радостей'])
    s5 = random.choice(['И я ценю твой вклад в это', 'И это не без твоей помощи',
                        'И ты помог(ла) этому осуществиться', 'И только благодаря твоей поддержке, я справился(лась)'])

    s6 = random.choice(['От всей души', 'От всего сердца', 'Искренне', 'Затая дыхание',
                        'С надеждой на будущее', 'С любовью в сердце', 'Сердечно'])
    # Пусть
    s7 = random.choice(['у тебя все будет так, как ты захочешь', 'будет меньше грусти и забот и побольше радости',
                        'все твои мечты сбудутся', 'подарки сыпятся как из Рога изобилия', 'все планы реализуются',
                        'тебе всегда сопутствует удача', 'радость наполнит каждый твой день',
                        'улыбки будут чаще, а грусть останется в прошлом',
                        'все неприятности останутся в прошлом', 'плохое забудется, а хорошее приумножится'])
    # Желаю тебе, чтобы
    s8 = random.choice(['тебе всегда сопутствовала удача', 'вдохновение не покидало тебя',
                        'тебе удалось воплотить всё задуманное', 'о тебе слагали легенды', 'год принёс лишь радости',
                        'радостные дни сменялись ещё более радостными', 'реалии соответствовали ожиданиям',
                        'все твои родные были здоровы', 'ты никогда не болел(а)',
                        'здоровье было крепким и денег было достаточно', 'трудности тебя обходили стороной',
                        'в сердце не было зимы', 'в сердце была весна', 'в сердце было лето',
                        'было меньше дней холодных, злых людей',
                        'аромат мандаринов ещё долго сохранял атмосферу праздника',
                        'всё, что мы отдали, вернулось нам втройне'])
    # а новый год стал самым
    s9 = random.choice(['запоминающимся', 'ярким', 'удачным', 'добрым', 'денежным', 'тёплым',
                        'счастливым', 'прекрасным', 'изумительным', 'тёплым', 'красочным', 'самым', 'лучшим', 'сочным',
                        'сытным', 'душевным', 'волшебным', 'сказочным', 'успешным'])

    congrat = '<html><body><div width="800px">'
    congrat += s1+'(ая) ИМЯ ДРУГА!'+b
    congrat += 'Этот год был '+s2+', но '+ s3 + ' он был и ' + s4 + '. ' + s5 + '!' + b
    congrat += s6 + ' поздравляю тебя с праздником!'+ b +'Пусть ' + s7 + '! Желаю тебе, чтобы ' + s8 + ', а новый год стал самым ' + s9 + '!'+b
    congrat += 'С новым счастьем!'
    congrat += '<//div><//body><//html>'

    return congrat


@app.route('/')
def index():
    return generate_text()


if __name__ == '__main__':
    app.run()
