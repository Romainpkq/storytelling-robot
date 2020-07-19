from src.interactive_conditional_samples import interact_model
import re

raw_text = input("Please input a text as the start of the story:")
raw_text = "<|endoftext|>" + raw_text
top_k = 40
temperature = 0.9
model_name = "345MChinese"

# we are trying to find a list of stopwords
stopwords = ["sex", "kill"]

while raw_text:
    result = interact_model(raw_text=raw_text, model_name=model_name, temperature=temperature, top_k=top_k)
    i = 0
    for text in result:
        text1 = re.sub("[\s+\.\!\/_,$%^*(+\"\']+", " ", text)
        text1 = text1.split()
        i += 1

        for word in text1:
            if word in stopwords:
                continue

        break

    print(result[i - 1])

    raw_text = input("Please input another text")
