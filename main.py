from Irlen_Israel_Modules import *
import time

def main():
    pass
    app = GUI.App()
    app.start()
    print('manager:', app.manager)
    if app.manager is not None:
        app.manager.save_manager()




if __name__ == '__main__':
    main()
