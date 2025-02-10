import os
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from packages.linkedin import scrape_linkedin_profile


OPEN_API_KEY = os.environ["OPEN_API_KEY"]

if __name__ == "__main__":

    summary_template = """
        given the Linkedin information {information} about a person I want you to create:
        1. A short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini", api_key=OPEN_API_KEY)

    chain = summary_prompt_template | llm

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/cheslav-zhuravsky", mock=True
    )

    res = chain.invoke(input={"information": linkedin_data})

    print(res)
