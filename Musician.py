# Super Class for the instruments
# Keep the persons name

class Musician:

  solo = 'sad music sounds...'
  instrument = 'Nothing'

  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return 'Name: ' + self.name + '\nInstrument: ' + self.get_instrument

  def __str__(self):
    return self.name + ' on ' + self.get_instrument() + '\n'

  def play_solo(self):
    return self.__class__.solo

  def get_instrument(self):
    return self.__class__.instrument

if __name__ == "__main__":
  temp = Musician('C')
  print(temp.play_solo())
