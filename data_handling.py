# 1 Python Modules and data handling assignment

'''
Task 1 Your mood day:

    Problem Statement:
    Create a Python program using a custom module that asks the user how they are feeling today and responds with a custom message based on the mood entered.
'''
# Code Example:
        # mood_responses.py
# def mood_response(mood):
        # Implement your response logic here

    # main.py
    # import mood_responses
    # mood = input("How are you feeling today? ")
    # print(mood_responses.mood_response(mood))

'''
Expected Outcome: 
    The program should be able to take a user's mood as input (e.g., happy, sad, excited) and return a corresponding custom message.
'''

from mood_responses import mood_angry, mood_anxious, mood_happy, mood_nostalgic, mood_sad

def main():
    mood_tracker = {
    "happy": mood_happy,
    "sad": mood_sad,
    "angry": mood_angry,
    "nostalgic": mood_nostalgic,
    "anxious": mood_anxious
    }

    user_mood = input("How are you feeling?(happy/sad/angry/nostalgic/anxious): ")
    response = None
    for mood, function in mood_tracker.items():
        if mood in user_mood:
            response = function()
            break
    if response:
        print(response)
    else:
        print("I can't response to that, can you try again?")


if __name__=='__main__':
    main()





