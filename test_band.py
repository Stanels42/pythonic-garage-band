# Test Bands
import pytest

from Band import Band
from Guitarist import Guitarist
from Bassist import Bassist
from Drummer import Drummer
from Musician import Musician

##################
# Test Band Data #
##################

band_one = """
Catfish and the Bottlemen
Van McCann,Guitar
Jon Barr,Drums
Benji Blakeway,Bass
Bob Hall,Guitar
"""
band_two = """
Louis the Child

Robby,Bass
Freddy,Bass
"""

#####################
# Band Member Names #
#####################

def test_name_musician():
  musician_test_name = Musician('John')
  assert 'John' == musician_test_name.name

def test_name_bass():
  bass_test_name = Bassist('Paul')
  assert 'Paul' == bass_test_name.name

def test_name_guitar():
  guitar_test_name = Guitarist('George')
  assert 'George' == guitar_test_name.name

def test_name_drummer():
  drummer_test_name = Drummer('Ringo')
  assert 'Ringo' == drummer_test_name.name

def test_class_type():
  test_drummer = Drummer('Test Name')
  assert isinstance(test_drummer, Drummer)

########################
# Get Instrument Tests #
########################

def test_musician_instrument():
  test_musician = Musician('Name')
  assert 'Nothing' == test_musician.get_instrument()

def test_get_guitar():
  test_guitarist = Guitarist('Slash')
  assert 'Guitar' == test_guitarist.get_instrument()

def test_get_bass():
  test_bassist = Bassist('Who Plays Bass Again?')
  assert 'Bass' == test_bassist.get_instrument()

def test_get_drums():
  test_drummer = Drummer('Insert Name')
  assert 'Drums' == test_drummer.get_instrument()

##############
# Test Solos #
##############

def test_guitar_solo():
  test_guitarist = Guitarist('An Actual Ukulele')
  assert 'Guitar Sounds' == test_guitarist.play_solo()

def test_bass_solo():
  test_bassist = Bassist('A Really Big Ukulele')
  assert 'Bass Sounds' == test_bassist.play_solo()

def test_drum_solo():
  test_drummer = Drummer('Silence')
  assert 'LOUD NOISES' == test_drummer.play_solo()

def test_all_band_solos():
  test_band = Band('Test Band', [Guitarist('Wham'), Drummer('Bam'), Bassist('Shang-a-lang')])
  assert 'Guitar Sounds LOUD NOISES Bass Sounds ' == test_band.play_solos()

#################
# Band Creation #
#################

def test_band_name():
  test_band = Band('Capital Cities')
  assert 'Capital Cities' == test_band.name

def test_band_by_array():
  band_array = [Band('Beatles', [Musician('John'), Bassist('Paul'), Guitarist('George'), Drummer('Ringo')])]
  assert band_array == Band.all_bands

def test_band_by_data():
  band_array = [Band.create_from_data(band_one)]
  assert band_array == Band.all_bands

def test_multiple_bands_by_data():
  band_array = [Band.create_from_data(band_one), Band.create_from_data(band_two)]
  assert band_array == Band.all_bands

##################
#  Output Tests  #
##################

def test_str_output():
  test_band = Band.create_from_data(band_one)
  expected = """The Band's Name is: Catfish and the Bottlemen

The Members are:
Van McCann on Guitar
Jon Barr on Drums
Benji Blakeway on Bass
Bob Hall on Guitar
"""
  assert expected == test_band.__str__()

def test_diff_str_output():
  test_band = Band.create_from_data(band_two)
  expected = """The Band's Name is: Louis the Child

The Members are:
Robby on Bass
Freddy on Bass
"""
  assert expected == test_band.__str__()

def test_all_bands_list():
  Band.create_from_data(band_one)
  Band.create_from_data(band_two)
  expected = """The Band's Name is: Catfish and the Bottlemen

The Members are:
Van McCann on Guitar
Jon Barr on Drums
Benji Blakeway on Bass
Bob Hall on Guitar


The Band's Name is: Louis the Child

The Members are:
Robby on Bass
Freddy on Bass


"""
  assert expected == Band.to_list()



@pytest.fixture(autouse = True)
def clean():
  Band.all_bands = []
