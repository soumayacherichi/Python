class User:		
    def __init__(self,first,last,mail, age, member, points):
        self.first_name = first
        self.last_name = last
        self.email = mail
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(f"User fullname is {self.first_name} {self.last_name} email {self.email} and has  {self.age} old ! he is{self.is_rewards_member}  and has {self.gold_card_points} points")
        return self
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return(self)
    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        return(self)
    def logic_member(self):
        if self.is_rewards_member == False:
            self.gold_card_points = 200

soumaya = User("Soumaya", "Cherichi", "Soumayacherichi@gmail.com", 35, True, 120)
soumaya.display_info()
soumaya.enroll().display_info()
soumaya.enroll().display_info().spend_points(10).display_info()
mohamed = User("Mohamed", "Ouergli","wergli7100@gmail.com",37,True,180)
mohamed.enroll().display_info().spend_points(80).display_info()
mohamed.display_info().spend_points(80).display_info().logic_member()
mohamed.display_info()
