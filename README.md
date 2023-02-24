# JobGPT

Chat GPT backed semantic search on LinkedIn job postings.

## Current experience and painpoint

Currently LinkedIn doesn't offer a very relavant search experience for job posting (this, I believe, is the same for other job sites as well). Part of it is due to lack of even more granular filters, and another part of it due to different job posts set different terms for same title. E.g. a simple software engineer could mean from front-end to full stack to backend not to mention all possible combinations of tech involved. So a customer, e.g. a SDE like you and I have to read line by line to understand the expectations for any titles.  

## Solution

This is where ChatGPT comes into play. By leveraging a full documentation semanic search, it can extract relevant job information and reformat job description to your liking.

## Prerequisites

### Prerequisite: Python dependencies

First ensure your python version is 3.10+.  Run `pip install -r requirements.txt` in folder.

### Prerequisite: OpenAI

Create a json file named `openai.json` under the same folder as `jobGpt.ipynb`. Use this format:

```json
{"OPENAI_API_KEY":"your_api_key"}
```

You can get your api key from [here](https://platform.openai.com/account/api-keys); click create new secret key and save it as above.

### Prerequisite: Selenium

Here I use Chrome as webdriver (bot controlled browser), you can use your own browser by changing this line:

```python
driver = webdriver.Chrome('./chromedriver.exe')
```

to  

```python
webdriver.your_browser('./your_driver_location.exe')
```

Say you go with Chrome (or you just want to it to run), download Chromedriver from [here](https://chromedriver.chromium.org/downloads). **Webdriver version has to match your Chrome version!** You can check your chrome version by this link: [chrome://settings/help](chrome://settings/help). After download move it to the same folder as `jobGpt.ipynb` and rename as `chromedriver.exe` if not already.

### Prerequisite: Google Sheets

Follow [this guide](https://developers.google.com/sheets/api/quickstart/python) right after [this part](https://developers.google.com/sheets/api/quickstart/python#authorize_credentials_for_a_desktop_application). Create a new Google Sheets and copy paste your sheet id to `SPREADSHEET_ID`.  

## The point: the future of search and the future of LLM

Paul Graham said for years how [Google search experience deteriorate](https://twitter.com/paulg/status/1477760548787920901?s=20) and how there could be a new start-up disrupt the status quo. My theory is, Google Search may be bad but it does have a big moat by being in the game and sharpening its tech long enough. There're way worse search engines out there, just think about `Cmd+f` for you text.  
So why don't we plug everything onto OpenAI LLM and call that a day? Other than the obvious fact that Microsoft/Bing forged an alliance with OpenAI with lots of cash and lots of GPUs, at this point it's still so expensive running an LLM. So far I don't have a price calculation of OpenAI api calls in bulk(tbd once foundry is out), but the individual api call is costing \$0.02 per 1k tokens, and each job post already consumes 4k which is $0.08. Not to mention if you want an actual experience similar to current LinkedIn filter you need to do it quick and across so many job posts. Say if you can only retrieve 4 post per 100, and you want to return 25 jobs matching the queries, then you end up with a cost of `25/4*100*0.08=50`. That's already more expensive than LinkedIn premium per month.
So my predictions are: in short run most search products are going through a semantic search or out battle. Google search probably will still stay relevant. To quote *the Double Helix* and change the subject matter to Google,

> The position would be far safer if Google had been merely
wrong instead of looking like a fool. Soon, if not already, he would be at it day and night.

Bing being the contender. A bunch of search engine start ups on the horizon (we're talking about Neeva and You) trying to blitzscale into mass majorities' consciousness. Outside of the main battle field, there'll be one million apps with VC dry powder ready to take NLP models and semantic search and a better UX into each individual siloed teritory and change the landscape. But in the long run the winner
is whoever able to shrink the inference cost by 10x. It would be really fun to see if one of these MLEs got fired by Google/Amazon/Microsoft actually possess that kind of knowledge and take this opportunity to become the next king.  