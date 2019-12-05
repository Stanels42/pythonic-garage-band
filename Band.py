class Band:

  all_bands = []

  def __init__(self, name, members = []):
    self.name = name
    self.members = members

  def __repr__(self):
    pass

  def __str__(self):
    pass

  @classmethod
  def to_list(cls):
    pass

  @staticmethod
  def create_from_data(data):
    pass
