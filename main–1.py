class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = int(age)
        self.tracks = tracks
        self.score = score
        
        
    def change_name(self, name):
        self.name = name
        print(self.name)
        
    
    def add_track(self, new_track):
        self.new_track = new_track
        print(self.new_track)
        
    def get_score(self):
          print(self.score)
            


    def change_age(self, age):
        self.age = age
        print(self.age)
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
