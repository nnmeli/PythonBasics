"""
Project 3 - EuroLeague

"""

my_name = "Muhammet Melih Tumur"
my_id = "200102002036"
my_email = "m.tumur2020@gtu.edu.tr"
import random 

class Person:
    def __init__(self, name , lastname):
        self.name = name 
        self.lastname= lastname
        
        
    def get_name(self):
        return f"{self.name} {self.lastname}" 
    
    def __str__(self):
        return f"{self.name} {self.lastname}" 
    
    
    
    def __lt__(self,other):
        if (self.lastname==other.lastname)==True:
            return self.name<other.name
        else :
            return self.lastname<other.lastname
"""
inst  = Person('Dimitris', 'Diamantidis') 
inst2 = Person('Juan Carlos', 'Navarro')
print(inst)
print(inst.get_name())
print(inst < inst2)
"""

class Player(Person):
      
    id1=1
    def __init__(self,name,lastname):
      self.name = name 
      self.lastname= lastname
      self.shoot_power= random.randint(4, 8)
      self.id=Player.id1
      self.haftalık_katkı=[]
      self.team=""
      Player.id1+=1
      
      
      
   
    def get_power(self):
      return self.shoot_power 
  
    def get_id(self):
        return self.id 
    def set_team(self, t):
        self.team=t
        
    
    def skor_yapıcı(self , x):
        
        sayi = x.get_power() + random.randint(-5, 5)
        self.haftalık_katkı.append(sayi)
        return sayi 
    def get_team(self):
        return self.team
        

class Manager(Person):
      id1=1
      def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname
        self.etki_listesi=[]
        self.id=Team.id1
        self.team=""
        Team.id1+=1
    
      def set_team(self , t):
        self.team=t
      
         
      def skor_yapici(self):
          
          sayi =  random.randint(-10, 10)
          self.etki_listesi.append(sayi)
          return sayi 
          
      def get_influence_detailed(self):
          return self.etki_listesi
      
      def get_id(self):
          return self.id    
      
      def get_team(self):
          return self.team
      
      def get_influence(self):
          return sum(self.etki_listesi)
      
      def __lt__(self,other):
           if (sum(self.etki_listesi)==sum(other.etki_listesi))==False:
               return self.etki_listesi<other.etki_listesi
               
           elif (self.lastname==other.lastname)==True:
               return self.name<other.name
           else :
               return self.lastname<other.lastname
            

class Team:
    
    id1=1
    def __init__(self ,teamname , manager , players):
        self.teamname=teamname
        self.manager=manager 
        p_list=[]
        for i in players:
          p_list.append(i)
        self.players=p_list
        self.id=Team.id1
        self.scores=[]
        self.yenilen=[]
        self.wins=0
        self.losses=0
        Team.id1+=1
    
    def get_name(self):
      return self.teamname
    
    def get_roster(self):
      return self.players
   
    def get_manager(self):
      return self.manager
     
    def get_id(self):
        return self.id 
    
    def powers(self):
        liste=[]
        for i in self.players :
            liste.append(i.get_power)
        return liste 
    def __str__(self):
        return self.teamname
    def get_scored(self):
        return sum(self.scores)
    def get_conceded(self):
        return sum(self.yenilen)
    def get_wins(self):
        return self.wins
    
class Match:
    def __init__(self ,home_team, away_team, week_no):
        self.home_team=home_team
        self.away_team=away_team
        self.week_no=week_no
        self.score=()
        self.played=False
    def play(self):
        
      
    
        h_a = self.home_team.get_manager().skor_yapici()
        a_a = self.away_team.get_manager().skor_yapici()     
        
        h_c=[]
        for i in range(4):
            for i in range(len(self.home_team.get_roster())):
                h_c.append(self.home_team.get_roster()[i].skor_yapıcı(self.home_team.get_roster()[i]))
            
        a_c=[]
        for i in range(4):    
            for i in range(len(self.away_team.get_roster())):
                a_c.append(self.away_team.get_roster()[i].skor_yapıcı(self.away_team.get_roster()[i]))
                
            
        ev_skor = sum(h_c)+h_a
        self.home_team.scores.append(ev_skor)
        self.away_team.yenilen.append(ev_skor)
        dep_skor = sum(a_c)+a_a
        self.away_team.scores.append(dep_skor)
        self.home_team.yenilen.append(dep_skor)
        
        if ev_skor == dep_skor:
            for i in range(len(self.away_team.get_roster())):
                a_c.append(self.away_team.get_roster()[i].skor_yapıcı(self.away_team.get_roster()[i]))
            for i in range(len(self.home_team.get_roster())):
                h_c.append(self.home_team.get_roster()[i].skor_yapıcı(self.home_team.get_roster()[i]))
                
            
        
        
        
        self.score = ev_skor,dep_skor
        self.played=True
        
        
        if self.score[0]>self.score[1]:
          self.home_team.wins +=1   
          self.away_team.losses +=1 
        elif self.score[1]>self.score[0]:
          self.away_team.wins +=1
          self.home_team.losses +=1
    
    
    def get_match_score(self):
        return self.score
    def get_teams(self):
        return self.home_team , self.away_team
    def get_home_team(self):
        return self.home_team
    def get_winner(self):
      if self.score==():
        return None
      elif self.score[0]>self.score[1]:        
        return self.home_team
      elif self.score[1]>self.score[0]:      
        return self.away_team  
      elif self.score()==():
        return None
    def is_played(self):
        return self.played
    def __str__(self):
        if self.played==False:
          return f"{self.home_team} vs {self.away_team}"
        elif self.played==True:
          return f"{self.home_team}({self.score[0]}) vs {self.away_team}({self.score[1]})"



"""
fb_players = [Player('Jan', 'Vesely'),

Player('Achille', 'Polonara'),
Player('Marko', 'Guduric'),
Player('Marial', 'Shayok'), Player('Nandode', 'Colo')]
fb_manager = Manager('Sasa', 'Dordevic')
team1 = Team('Fenerbahce Beko Istanbul',fb_manager, fb_players)

ab_players = [Player('Jaasdsan', 'Vesasdasely'),
Player('Acasdasdille', 'Poloasdasdnara'),
Player('Markasdasdo', 'Gudasdasduric'),
Player('Masdasdarial', 'Shaasdasyok'), Player('Nandasdasdode', 'Colasdasdo')]
ab_manager = Manager('Saasdasdsa', 'Dordasdasdevic')
team2 = Team('MelihBahce',ab_manager, ab_players)

m = Match(team1,team2,1)
print(m.get_home_team())
m.play()
print(m.get_match_score())
print(m.get_winner())
print(m.is_played())
print(m)
print(team1.get_scored())
print(team1.get_wins())


inst = Player('Dimitris', 'Diamantidis')
inst.set_team(team1)
print(inst.get_team())
"""





