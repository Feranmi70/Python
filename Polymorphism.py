class cow:
    def tastiness(self):
        print ("This is Delicious")
    def texture(self):
        print("This is Tender")
class chicken:
    def tastiness(self):
        print ("This is Alright")
    def texture(self):
        print("This is Chewy")
class pig:
    def tastiness(self):
        print ("This is Ok")
    def texture(self):
        print("This is Crunchy")      
class goat:
    def tastiness(self):
        print ("This is Awesome")
    def texture(self):
        print("This is soft")
def animals(animal):
    animal.tastiness()

cowobj = cow()
chickenobj = chicken()
pigobj = pig()
goatobj = goat()

animals(cowobj)
animals(chickenobj)
animals(pigobj)
animals(goatobj)