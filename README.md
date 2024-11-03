# Headless Browser E2E Test Agent
An intelligent agent designed to control a headless browser and perform end-to-end (E2E) testing on web pages. Users can specify the webpage URL and describe test cases in natural language. The agent will interpret these instructions, generate, and execute the tests.

**Tech Stack**
- [LangGraph](https://langchain-ai.github.io/langgraph/) - agent implementation
- [Playwright](https://github.com/microsoft/playwright-python) - a Python Playwright version that we can use to generate a script that can execute the test
- [Taipy](https://taipy.io/) - A library that we will use to spin up a simple website where we can demonstrate the capability of our agent
- [langchain_community.agent_toolkits.PlayWrightBrowserToolkit](https://python.langchain.com/v0.1/docs/integrations/toolkits/playwright/)

**Use Case**
- Analyze a website with the Agent
- Create E2E tests in the Python Playwright version of the package
- Execute the generated test cases
- Provide reports based on the results of the tests

## Development

### Setup Environment
Create a new conda environment with Python 3.11
```
conda create --name e2e_agent python=3.11
```
Activate the environment
```
conda activate e2e_agent
```
Install the required packages
```
pip install -r requirements.txt
```