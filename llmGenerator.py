import openai
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()  # Load variables from .env

openai.api_key = os.getenv("OPENAI_API_KEY")

# client = OpenAI()
# def llmGenerator(inputText):
#   client = OpenAI()

#   response = client.chat.completions.create(
#     model="gpt-4o",
#     messages=[
#       {
#         "role": "user",
#         "content": [
#           {
#             "type": "text",
#             "text": f"Transform the following passage into uzz-ified slang where possible. Apply the '-uzz' suffix to words that can naturally carry it, especially casual or slang terms. Keep the meaning intact and don't overdo it with '-uzz' additions. Here's the text: '{inputText}'"
#           }
#         ]
#       }
#     ],
#     temperature=1,
#     max_tokens=2048,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0,
#     response_format={
#       "type": "text"
#     }
#   )

#   generation = response.choices[0].message.content

#   print(generation)

#   return generation

# # if __name__ == "__main__":
# #   jobDesc = """I love my homies so much and I wish them merry christmas"""

# #   llmGenerator(jobDesc)

# from openai import OpenAI
# client = OpenAI()

def llmGenerator(inputText):
  client = OpenAI()

  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": f"You are an \"Uzz\" words generator. Given a sentence, enclosed within 3 backticks, you will uzzify it \n\n-Uzz, also known as Uzz Words or Words That End In -Uzz, refers to the \"-uzz\" suffix used to make portmanteaus of the slang term huzz, meaning \"hoes.\" Huzz started as an AAVE slang term popularized by Twitch streamer Kai Cenat. In late 2024, huzz memes went viral on TikTok and a slew of words ending with \"-uzz\" like bruzz (broes) were created. Other Uzz Words include \"gruzz, (grandma hoes)\" \"fuzz\" (freshmen hoes) and \"chuzz,\" (chopped hoes) among others.\n\nHere is the sentence: \n```{inputText}. Generate your response as a JSON.```"
          }
        ]
      }
    ],
    response_format={
      "type": "text"
    },
    temperature=1,
    max_completion_tokens=10000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  generation = response.choices[0].message.content

  # Remove the ```json at the beginning and closing backticks
  generation_cleaned = re.sub(r'^```json\n', '', generation)  # Remove opening block and json specifier
  generation_cleaned = re.sub(r'```$', '', generation_cleaned)  # Remove closing backticks

  print("the generation:", generation_cleaned)

  # Parse the JSON string
  generation_JSON = json.loads(generation_cleaned)

  print(inputText)

  print(generation_JSON)

  return generation_JSON["uzzified_sentence"]
