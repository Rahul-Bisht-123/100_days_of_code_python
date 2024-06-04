class Animal:
  def __init__(self) -> None:
    self.eyes_count = 2
  
  def running(self):
    print("Animal is running")

class Goat(Animal):
  def __init__(self) -> None:
    super().__init__()

  def running(self):
    super().running()
    print("wooo")
    
  def legs(self):
    print("Goat has 4 Legs")


goat = Goat()
goat.running()