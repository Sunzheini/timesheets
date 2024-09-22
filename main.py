from core.database_controller import DatabaseController
from core.engine import Engine
from db.database import DataBase
from gui.gui_controller import MyGui


if __name__ == '__main__':
    database = DataBase()
    db_controller = DatabaseController(database)
    engine = Engine(db_controller)
    gui_controller = MyGui(engine)
    gui_controller.run()
