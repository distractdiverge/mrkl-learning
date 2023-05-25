from langchain import tool

from pydantic import BaseModel, Field

from github import Github

class CreateGitRepoInput(BaseModel):
    name: str = Field(description="should be a valid repo name")
        
@tool("create_git_repo", return_direct=True, args_schema=CreateGitRepoInput)
def create_git_repo(name: str) -> str:
    """Creates a git repository under the configured user with the given name."""
    g = Github("ACCESS_TOKEN")
    repo = g.create_repo(name)
    url = repo.git_url
    return url