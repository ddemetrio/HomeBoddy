from enum import Enum, unique


class BasicChoices(Enum):
    """ Basic Choices for the questions"""
    yes = 'Yes'
    no = 'No'
    not_sure = 'Not sure'


@unique
class Questions(Enum):
    """ Answer choices for the questions """
    question_0 = {
        'title': 'What is your ZIP Code?'
    }
    question_1 = {
        'title': 'Which feature is most important to you?',
        'choice_1': 'Ease of use',
        'choice_2': 'Safer bathing',
        'choice_3': BasicChoices.not_sure.value
    }
    question_2 = {
        'title': 'Describe your project.',
        'choice_1': 'Tub to walk-in shower',
        'choice_2': 'Shower to walk-in shower',
        'choice_3': BasicChoices.not_sure.value
    }
    question_3 = {
        'title': 'Select your shower layout.',
        'choice_1': 'Against 1 wall',
        'choice_2': 'Against 2 walls',
        'choice_3': BasicChoices.not_sure.value
    }
    question_4 = {
        'title': 'Are you the homeowner or authorized to make property changes?',
        'choice_1': BasicChoices.yes.value,
        'choice_2': BasicChoices.no.value,
        'message': 'Our installers require the homeowner or someone authorized to make property changes be present '
                   'during the estimate. Would you like to continue?'
    }
    question_5 = {
        'title': 'Is it a mobile, modular or manufactured home?',
        'choice_1': BasicChoices.yes.value,
        'choice_2': BasicChoices.no.value,
        'message': 'Unfortunately, our installers do not work with mobile, modular or manufactured homes. '
                   'Would you still like to continue?'
    }
    question_6 = {
        'title': 'Is there an existing bathtub or shower that we would be replacing?',
        'choice_1': BasicChoices.yes.value,
        'choice_2': BasicChoices.no.value,
        'message': 'Unfortunately, our installers can only replace an existing bathtub or shower. '
                   'Would you still like to continue?'
    }
    question_7 = {
        'title': 'Is this request covered by an insurance or VA claim?',
        'choice_1': BasicChoices.yes.value,
        'choice_2': BasicChoices.no.value,
        'message': 'Unfortunately, our installers do not currently work with insurance or VA claims. '
                   'Would you still like to continue?'
    }
    question_8 = {
        'title': 'Seniors and the military (active/retired/spouses) get an extra 10% OFF!',
                 'Seniors and the military (active/retired/spouses) get an extra 10% OFF!'
        'choice_1': 'Senior 65+',
        'choice_2': 'Military personnel, veteran or spouse',
        'choice_3': 'None of the above'
    }
    question_9 = {
        'title': 'Who should I prepare this estimate for?'
    }
    question_10 = {
        'title': 'What is your phone number?'
    }
    question_11 = {
        'title': 'Please confirm your phone number.'
    }


title_final_answer = 'Thank you {}, your contractor QA Customer will call soon!'
title_answer_sorry = 'Sorry to see you go!'
title_cancel_project = 'We just need to confirm your information to get you a quote.'
title_no_contractors = 'Unfortunately, I have no matching contractors in your area yet.'
title_thank_you_for_your_interest = 'Thank you for your interest, we will contact you when our ' \
                                    'service becomes available in your area!'
