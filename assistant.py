import pyttsx3
from datetime import datetime
import speech_recognition as sr


# initializing the engine of the speak function
engine = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
# there are two type of voices male or female 0==female, 1==male
engine.setProperty('voices', voices[0].id)
def speak(audio):
    '''
    this fuction converts text to the audio
    '''
    engine. setProperty("rate", 178)
    engine.say(audio)
    engine.runAndWait()
def wish_me():
    '''
    this function will wish me first
    according to the time
    '''
    hour_is = int(datetime.now().hour)
    if hour_is<12:
        # morning
        speak(f'good morning sir the time is {datetime.now()} what would you like to do today...')
    elif hour_is>=12 and hour_is<15:
        # after noon
        speak(f'good afternoon sir the time is {datetime.now()} what would you like to do today...')
    elif hour_is>=15 and hour_is<19:
        # evening
        speak(f'good evening sir the time is {datetime.now()} what would you like to do today...')
    elif hour_is>=19 and hour_is<24:
        # night
        speak(f'good night sir the time is {datetime.now()} what would you like to do today...')
def take_command():
    '''
    this fuction take the voice input in from the user
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, len='en-in')
        print(f'you said : {query}')
    except Exception as e:
        print("sorry i can't recognize, say that again please...")
        speak('yes')
        return 'None'
    return query


class Mathametics():
    def factorial(self, num):
        '''
        this fuction is used for calculate
        the factorial the entered number
        '''
        fact = 1
        for i in range(1, num+1):
            fact = fact*i
        speak(f'the factorial of the number is {fact}')
        take_command()
    def calculate(self, num1, num2, operator):
        '''
        this function is used as a calculator
        take three intences number one, number two and the operator
        '''
        # add
        if operator=='+':
            result = num1+num2
        # minus
        elif operator=='-':
            result = num2-num1
        # multiply
        elif operator=='*':
            result = num2*num1
        # divide
        elif operator=='/':
            result = num2/num1
        # remainder
        elif operator=='%':
            result = num2%num1
        speak(f'the result is {result}')
        take_command()
    def hypotenus(self, p, b):
        '''
        this functions is used for calculate
        the length of hypotenus of a right angle triangle
        take length of perpendicular and base
        '''
        # square of H == square of p + square of b
        h = (p*p)+(b*b)
        # now we have to find how can we calculate the square root of h
        # search google
        length_hypotenus = 0
        print(length_hypotenus)
    def triangle_angle(self, first_angle, second_angle):
        '''
        this is used for calculate
        the thrid angle of a triangle
        when other two were given
        '''
        # the sum of all angles in a triangle is 180 degree.
        third_angle = 180 - (first_angle+second_angle)
        print(third_angle)
    def quadrilatral_angle(self, first_angle, second_angle, third_angle):
        '''
        this is used for calculate
        the fourth angle of the quadrilatral
        '''
        # sum of all angles in an quadrilatral is equal to 360 degree
        fourth_angle = 360-(first_angle+second_angle+third_angle)


class Draw_pattern():
    def  pattern(self, num):
        pass
                           


if __name__ =='__main__':
    wish_me()
    while True:
        query = take_command().lower()

        if("what's your name") in query:
            speak('my name is assistant and i programmed to make things simple...')
        elif "will you be my girlfriend" in query:
            speak('sorry, i have boyfirend...')
        elif "can you calculate somthing for me" in query:
            speak('yes i can...')
            speak('enter the numbers seprated by a space...')
            nums = input().split(' ')
            num1 = nums[0]
            num2 = nums[1]
            speak('now enter the operator')
            operator = input()
            Mathametics().calculate(num1, num2, operator)
        elif 'can you print a pattern for me' in query:
            speak('''yeah sure..., the pattern i can print is a square,
                     right angle triangle,
                     or reverse right angle triangle
                     and i can also print a alphabet rangoli if you want...''')
            

