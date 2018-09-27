from setuptools import setup, find_packages

setup (
   name='Bounce',
   version='0.3',
   packages=find_packages(),

   # Declare your packages' dependencies here, for eg:
#       install_requires=['foo>=3'],

   # Fill in these to make your Egg ready for upload to
   # PyPI
   author='rada',
   author_email='rada.telyukova@gmail.com',

   #summary = 'Just another Python package for the cheese shop',
   url='rada.telyukova.com/not-exists',
   license='MIT',
   long_description='''Game: hit the ball.
   The ball flies around the screen, the player must hit it by the bat.
   If the ball reaches the bottom of the screen, the game is over

   Source: "Python for Kids" by Jason R.Briggs'''
)