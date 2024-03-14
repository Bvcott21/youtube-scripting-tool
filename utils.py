from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.tools import DuckDuckGoSearchRun

# Function to generate video script
def generate_script(prompt, video_length, creativity):
    # Template for generating 'title'
    title_template = PromptTemplate(
        input_variables = ['subject'],
        template = 'Please come up with a title for a YouTube video on {subject}'
    )
    
    #Tempalte for generating video script using engine search
    script_template = PromptTemplate(
        input_variables  = [
            'title',
            'DuckDuckGo_Search',
            'duration'],
        template = '''Create a script for a YouTube video based on this title.
        TITLE: {title}, 
        
        of duration: {duration} minutes, 
        
        using this search data {DuckDuckGo_Search}
        '''
    )
    
    # Setting up OpenAI LLM
    llm = OpenAI(temperature = creativity,
                model_name = 'gpt-3.5-turbo')
    
    # Creating chain for 'Title' & 'Video Script'
    title_chain = LLMChain(llm = llm,
                        prompt = title_template,
                        verbose = True)
    
    script_chain = LLMChain(llm = llm,
                        prompt = script_template,
                        verbose = True)
    
    # https://python.langchain.com/docs/modules/agents/tools/integrations/ddg
    search = DuckDuckGoSearchRun()
    
    # Executing the chains we created for 'Title'
    title = title_chain.run(prompt)
    
    # Executing the chains we creted for 'Video Script' by taking help of search 
    # engine DuckDuckGo
    search_result = search.run(prompt)
    script = script_chain.run(title = title,
                            DuckDuckGo_Search = search_result,
                            duration = video_length)
    
    # Returning the output
    return search_result, title, script