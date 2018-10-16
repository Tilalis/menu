from pony import orm

db = orm.Database()
db.bind(provider='postgres', user='postgres', password='', host='127.0.0.1', port='5432', database='postgres')


class Restaurant(db.Entity):
    name = orm.Required(str)
    menu = orm.Set('MenuItem')


class Category(db.Entity):
    name = orm.Required(str)
    menu_items = orm.Set('MenuItem')


class Modifier(db.Entity):
    name = orm.Required(str)
    calories = orm.Required(int)
    menu_items = orm.Set('MenuItem')
    modifies = orm.Set('Modifier', reverse="modifiers")
    modifiers = orm.Set('Modifier', reverse="modifies")


class MenuItem(db.Entity):
    restaurant = orm.Required(Restaurant)
    name = orm.Required(str)
    description = orm.Required(str)
    category = orm.Required(Category)
    calories = orm.Required(int)
    price = orm.Required(float)
    modifiers = orm.Set(Modifier)


with db.set_perms_for(Restaurant, Category, Modifier, MenuItem):
    orm.perm("view", group="anybody")

db.generate_mapping(create_tables=True)
