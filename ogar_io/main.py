from multiprocessing import Process

from api import app, queue
from game import OgarIOGame


def run_game(queue):
    OgarIOGame(queue).start()


game = Process(target=run_game, args=(queue,))
game.start()

app.run(debug=False, host='0.0.0.0')
