class Params():
    def __init__(self):
        self.BATCH_SIZE = 128
        self.START_LEARNING_RATE = 0.01
        self.EPOCHS = 500
        self.SR = 8000
        self.MFCC = True
        self.N_COMPONENTS = 40
        self.WINDOW_SIZE = 25
        self.STEP_SIZE = 10

        self.MAX_LENGTH = 8000

        self.N_PRODUCERS = 4
        self.MULTIPROCESS = False


params = Params()
