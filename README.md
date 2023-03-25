# mybing | A command line client of ChatGPT using bing prompt

This is a quick command line chatGPT using Bing's instrctuions.

Disclaimer: This is not Bing and it is not associated with microsoft at all. It is just the raw GPT-4 model using a Bing prompt. I was able to extract Bing's own instructions, and this chatbot is utilizing those instructions. However, the raw GPT-4 model does not have access to Bing's fine-tuned models or post-processing capabilities.

Upon experimentation, it appears that Bing is utilizing a model that has been fine-tuned to generate actions such as #inner_monologue, #search_query, #search_results, #message, #suggestions, or #advertisements. You are welcome to inspect the **prompt.md** file to view the prompt that Microsoft was using on **March 25th, 2023.**


## Usage:
```
pip install -r requirements.txt 
export OPENAI_API_KEY=<YOUR API KEY>
python3 mybing.py
```




