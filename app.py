'''
Задание

Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
 и дочерние шаблоны для страниц категорий товаров и отдельных товаров. 
 Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.
 
'''


from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')


@app.route('/clothes/')
def get_clothes():
    clothes = ({'title': 'clothe1', 'material': 'cotton', 'price':"15.50$"},
               {'title': 'clothe2', 'material': 'kashmir', 'price': "40.90$"},
               {'title': 'clothe3', 'material': 'cotton', 'price': "25.25$"})
    
    return render_template('clothes.html', clothes=clothes)


@app.route('/shoes/')
def get_shoes():
    shoes = ({'title': 'shoes1', 'material': 'leather', 'price': "40.50$"},
               {'title': 'shoes2', 'material': 'velvet', 'price': "60.90$"},
               {'title': 'shoes3', 'material': 'leather', 'price': "35.25$"})
    
    return render_template('shoes.html', shoes=shoes)

@app.route('/jackets/')
def get_jackets():
    jackets = ({'title': 'jacket1', 'material': 'cotton', 'price': "50.50$"},
               {'title': 'jacket2', 'material': 'leather', 'price': "120.90$"},
               {'title': 'jacket3', 'material': 'velvet', 'price': "80.25$"})
    
    return render_template('jackets.html', jackets=jackets)



if __name__ == '__main__':
    app.run(debug=True)
