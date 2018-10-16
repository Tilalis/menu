from models import *
from pony import orm


@orm.db_session
def createdb():
    la_scala = Restaurant(name="La Scala")
    wok = Restaurant(name="The WOK")

    category_pizza = Category(name="Pizza")
    category_wok = Category(name="Wok")

    cheese = Modifier(name="Cheese", calories=259)
    ketchup = Modifier(name="Ketchup", calories=50)
    mayo = Modifier(name="Mayo", calories=105)
    beef = Modifier(name="Beef", calories=533)
    chicken = Modifier(name="Chicken", calories=432)
    spicy_seasoning = Modifier(name="Spicy Seasoning", calories=7)
    russian_dressing = Modifier(name="Russian Dressing", modifiers=[ketchup, mayo], calories=80)


    ketchup_pizza = MenuItem(
        restaurant=la_scala,
        category=category_pizza,
        calories=350,
        price=5.55,
        name="Ketchup Pizza",
        description="Let us be honest. We just added more ketchup to Margarita. You gonna like it.",
        modifiers=[ketchup, cheese]
    )

    russian_pizza = MenuItem(
        restaurant=la_scala,
        category=category_pizza,
        calories=255,
        price=8.95,
        name="Russian Pizza",
        description="There is no russian in margarita with russian dressing and you know it.",
        modifiers=[russian_dressing, cheese]
    )

    wok_chicken = MenuItem(
        name="Wok Spicy Chicken",
        restaurant=wok,
        category=category_wok,
        calories=112,
        price=12.98,
        description="Don't even dare to try it. Too spicy for you, chicken!",
        modifiers=[chicken, spicy_seasoning]
    )

    wok_beef = MenuItem(
        name="Wok Beef",
        restaurant=wok,
        category=category_wok,
        calories=150,
        price=6.79,
        description="Gonna order it because you're afraid of spicy chicken, chicken?",
        modifiers=[beef]
    )


if __name__ == '__main__':
    createdb()
