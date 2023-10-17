from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from configparser import ConfigParser
import os
from third_party.linkedin import scrape_linkedin_profile

parser = ConfigParser()
_ = parser.read("./.cfg.ini")

# gpt3 api key
openai_api_key = parser.get("openai", "api_key")

os.environ["OPENAI_API_KEY"] = openai_api_key

if __name__ == "__main__":
    print("Hello LangChain")

    summary_template = """
        given the linkedin information {information} about a person, go ahead and provide me with:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linked_data = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/harrison-chase-961287118/"
    )

    print(chain.run(information=linked_data))
