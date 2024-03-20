from core.database_controller import DatabaseController
from core.engine import Engine
from gui.gui_controller import MyGui


if __name__ == '__main__':
    db_controller = DatabaseController()
    engine = Engine(db_controller)
    gui_controller = MyGui(engine)
    gui_controller.run()
