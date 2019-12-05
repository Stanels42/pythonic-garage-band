# Super Class for the instruments
# Keep the persons name

class Musician:

  solo = 'sad music sounds...'
  instrument = 'Sadness'

  def __init__(self, name):
    self.name = name

  def play_solo(self):
    return self.solo

  def get_instrument(self):
    return self.instrument
