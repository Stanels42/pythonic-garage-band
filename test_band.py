# Test Bands


from Band import Band
from Guitarist import Guitarist
from Bassist import Bassist
from Drummer import Drummer
from Musician import Musician

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

#################
# Band Creation #
#################

