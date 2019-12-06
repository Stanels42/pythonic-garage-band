import re

from Guitarist import Guitarist
from Bassist import Bassist
from Drummer import Drummer
from Musician import Musician

class Band:

  all_bands = []

  def __init__(self, name, members = []):
    self.name = name
    self.members = members
    self.__class__.all_bands.append(self)

  def __repr__(self):
    output = 'Name: ' + self.name + '\n' + '# of members: ' + len(self.members)
    return output

  def __str__(self):
    output = 'The Band\'s Name is: ' + self.name + '\n\n'
    output += 'The Members are:\n'
    for person in self.members:
      output += person.__str__()
    return output

  def play_solos(self):
    output = ''
    for person in self.members:
      output += person.play_solo() + ' '

    return output

  @staticmethod
  def create_from_data(data):
    split_data = re.findall(r"\S.*", data)
    print(split_data)

    title = split_data[0]
    members = []
    for i in range(1, len(split_data)):
      current_member = split_data[i].split(',')

      if current_member[1] == 'Guitar':
        members.append(Guitarist(current_member[0]))
      elif current_member[1] == 'Bass':
        members.append(Bassist(current_member[0]))
      elif current_member[1] == 'Drums':
        members.append(Drummer(current_member[0]))
      else:
        members.append(Musician(current_member[0]))


    return Band(title, members)


  @classmethod
  def to_list(cls):
    output = ''
    for current_band in cls.all_bands:
      output += current_band.__str__() + '\n\n'

    return output


if __name__ == "__main__":

  band_one = """
  Catfish and the Bottlemen
  Van McCann,Guitar
  Jon Barr,Drums
  Benji Blakeway,Bass
  Bob Hall,Guitar
  """

  print(Band.create_from_data(band_one))

