import cohere
import pandas as pd
import os
API_KEY = "5wY9MBL5jqXzYP8khpDyHnwrovfpRi12jhPxJFiL"
print('hello')
print(API_KEY)

co = cohere.Client(API_KEY)

destinationExamples = [
    ("Toronto", "Plan me a trip to go to Toronto for 5 days."),
    ("Brazil", "I want to go to Brazil with a group of 5 friends."),
    ("Beijing", "Plan me a trip to see attractions around Beijing."),
    ("Egypt", "I am planning a trip this winter to go to Egypt with my family.")
]

costExamples = [
    ("1000", "Plan me a trip to go to Toronto for 5 days under 1000 dollars."),
    ("5000", "I want to go to Brazil with a group of 5 friends while spending less than $5000"),
    ("1023", "Plan me a trip less than 1023 yuan to see attractions around Beijing."),
    ("2500", "I am planning a trip this winter to go to Egypt with a budget of 2500 rupees with my family.")
]

timeExamples = [
    ("Jun 1 to Jun 5", "Plan me a trip to go to Toronto for 5 days from Jun 1 to Jun 5 with my girlfriend"),
    ("July 1 to August 31", "I want to go to Brazil with a group of 2 friends anytime during summer vacation."),
    ("October 2 to Oct 15", "Plan me a trip to see attractions around Beijing with my family of four people from Oct 2 to Oct 15."),
    ("Dec 25 to Jan 7", "I am planning a trip this winter break to go to Egypt with my family."),
    ("Mar 25 to Mar 31", "Plan a trip in the last week of March to hamilton for a budget of $1000"),
    ("Apr 24 to Apr 30", "Plan a trip in the last week of April to hamilton for a budget of $1000"),
    ("Jan 1 to Jan 7", "Plan a trip in the first week of December to hamilton for a budget of $1000")
]

peopleExamples = [
    ("Toronto", "Plan me a trip to go to Toronto for 5 days."),
    ("Brazil", "I want to go to Brazil with a group of 5 friends."),
    ("Beijing", "Plan me a trip to see attractions around Beijing."),
    ("Egypt", "I am planning a trip this winter to go to Egypt with my family.")
]

peopleExamples = [
    ("Toronto", "Plan me a trip to go to Toronto for 5 days."),
    ("Brazil", "I want to go to Brazil with a group of 5 friends."),
    ("Beijing", "Plan me a trip to see attractions around Beijing."),
    ("Egypt", "I am planning a trip this winter to go to Egypt with my family.")
]




pd.set_option('display.max_colwidth', None)

# def get_post_titles(**kwargs):
#     """ Gets data from the pushshift api. Read more: https://github.com/pushshift/api """
#     base_url = f"https://api.pushshift.io/reddit/search/submission/"
#     payload = kwargs
#     request = requests.get(base_url, params=payload)
#     return [a['title'] for a in request.json()['data']]


class cohereExtractor():
    def __init__(self, examples, example_labels, labels, task_desciption, example_prompt):
        self.examples = examples
        self.example_labels = example_labels
        self.labels = labels
        self.task_desciption = task_desciption
        self.example_prompt = example_prompt

    def make_prompt(self, example):
        examples = self.examples + [example]
        labels = self.example_labels + [""]
        print(self.task_desciption +
                "\n---\n".join( [examples[i] + "\n" +
                                self.example_prompt + 
                                 labels[i] for i in range(len(examples))]))
        return (self.task_desciption +
                "\n---\n".join( [examples[i] + "\n" +
                                self.example_prompt + 
                                 labels[i] for i in range(len(examples))]))

    def extract(self, example):
      extraction = co.generate( 
          model='medium',
          prompt=self.make_prompt(example),
          max_tokens=10,
          temperature=0.1,
          stop_sequences=["\n"])
          
      return(extraction.generations[0].text[:-1])


cohereDestinationExtractor = cohereExtractor([e[1] for e in destinationExamples], 
                                       [e[0] for e in destinationExamples], [],
                                       "", 
                                       "extract the destination from the post:")


cohereTimeExtractor = cohereExtractor([e[1] for e in timeExamples], 
                                       [e[0] for e in timeExamples], [],
                                       "", 
                                       "extract the destination from the post:")

cohereCostExtractor = cohereExtractor([e[1] for e in costExamples], 
                                       [e[0] for e in costExamples], [],
                                       "", 
                                       "extract the destination from the post:")

tripPrompt = "I want to go to Niagara Falls on Jan 14 to Jan 21 and I have a budget of under 1000 dollars for 5 people."
extracted_text = cohereDestinationExtractor.extract(tripPrompt)
print(extracted_text)

tripLength = cohereTimeExtractor.extract(tripPrompt)
print(tripLength)

cost = cohereCostExtractor.extract(tripPrompt)
print(cost)