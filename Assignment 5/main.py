import controller
from time import sleep


while True:

    cart = controller.Cart()

    sleep(1)

    while cart.stillAlive():
        cart.update(1)
        print('Theta =',cart.state[2])

        sleep(0.02)
