import sys, os
import random
#sys.stdout = open(os.devnull, 'w')

from transformers import pipeline, T5Tokenizer, T5ForConditionalGeneration

pipe_flan = pipeline("text2text-generation", model="google/flan-t5-base")
words = ["able","danger","hill","out","spring","about","dark","him","outside","square","above","daughter","himself","over","stairs","accident","day","hint","own","stairway","acid","decide","his","oxygen","stand","across","decided","history","page","stars","act","decimal","hold","paint","start","add","deep","hole","pair","state","admission","delivery","home","pants","statement","Africa","dentist","hope","paper","stay","after","deposit","horse","para"]
#input_text = "Hello, how are you doing?"

while True:
    #outputs = pipe_flan(input_text)
    outputs = pipe_flan(''.join(random.choice(words) for i in range(5)))
    #print(outputs) 
    #input_text = outputs[0]['generated_text']
