def get_steps(steps):
    if(steps <= 100000): return steps
    else : steps = 0      
    return steps
    
def getMenyu(calories):
    if(calories <= 1200): return 1200 
    if(calories <= 1600): return 1600
    if(calories <= 2000): return 2000
    if(calories <= 2400): return 2400
    if(calories <= 2900): return 2900
    if(calories <= 3400): return 3400
 
def get_gender(gender):
    if(gender == "male"): return "Мужской"
    else : return "Женский"

def get_activity(activity):
    ACTIVITY_CHOICES = { 'minimal': 'Сидячий режим весь день',
                        'low':'Минимальная активность',
                        'mid': 'Средняя активность',
                        'high': 'Тяжелая работа и/или нагрузка', 
                        'very_high': 'Экстрим'
    }
    return ACTIVITY_CHOICES.get(activity,'low')
def get_target(target):
    TARGET_CHOICES = {
        'trening':'Эктоморф, энергичный, худой, быстрый',
        'losing':'Эндоморф, полный, широкий и медлительный',
        'maintenance':'Мезоморф, достаточно мускулистый, средний'
    }
    return TARGET_CHOICES.get(target,'trening')

def get_rate(activity):
            rate = 0
            if activity == 'minimal':
                rate = 1
            elif  activity == 'low':
                rate = 2
            elif  activity == 'mid':
                rate = 3
            elif  activity == 'high':
                rate = 4
            elif  activity == 'very_high':
                rate = 5
            else:
                rate = 0
            return rate

def get_calories(self):
            if self.gender == 'male':
                calories = ((10 * self.weight) + 6.25 * self.height - 5 * self.age + 5) * get_rate(self.activity)
            else:
                calories = ((10 * self.weight) + 6.25 * self.height - 5 * self.age - 161) *  get_rate(self.activity)

            if(self.target == "trening"):
                calories *= 1.15
            else:
                if(self.target == "maintenance"):
                    calories *= 0.85
            return int(calories)