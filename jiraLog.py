from collections import Counter
from typing import cast

from jira import JIRA
from jira.client import ResultList
from jira.resources import Issue
import sys

JIRA_SERVER = ''
JIRA_USER = ''
JIRA_PASSWORD = ''

def getJiraMyselfInstance(username, password, server):
    # Some Authentication Methods
    jira = JIRA(
        basic_auth=(username, password),  # a username/password tuple [Not recommended]
        # basic_auth=("email", "API token"),  # Jira Cloud: a username/token tuple
        # token_auth="API token",  # Self-Hosted Jira (e.g. Server): the PAT token
        # auth=("admin", "admin"),  # a username/password tuple for cookie auth [Not recommended]
        server=server
    )

    # Who has authenticated
    myself = jira.myself()
    return myself

def failure(error):
    print("Command Incorrect")
    print(error)

def log_work_from_workflows(username, password, server, workflow):
    jiraInstance = getJiraMyselfInstance(username, password, server)
    for x in workflows[workflow]:
        print(x)
        jiraInstance.add_worklog(issue=x['issue'], timeSpent=x['length'])

def log_work_from_cli(username, password, server, ticket, length):
    jiraInstance = getJiraMyselfInstance(username, password, server)
    jiraInstance.add_worklog(issue=ticket, length=length)


def getArgument(position, default_value):
    if(len(sys.argv) > position):
        return sys.argv[position]
    else:
        return default_value


workflows = {
    'OOO': [{
        'issue': 'LIMA-9',
        'length': '8h',
        'startTime': '8:00'
    }],
    'normalWorkDay': [{
        'issue': 'LIMA-6',
        'length': '1h',
        'startTime': '10:00'
    },{
        'issue': 'LIMA-6',
        'length': '5h',
        'startTime': '10:00'
    }],
    'newWorkFlow': [{
        'issue': 'LIMA-6',
        'length': '1h',
        'startTime': '10:00'
    },{
        'issue': 'LIMA-6',
        'length': '5h',
        'startTime': '10:00'
    }]
}

command_one = getArgument(1, 'help')
if(command_one):
    if(command_one == "workflow"):
        command_two = getArgument(2, '')
        if(command_two != '' and command_two in workflows.keys()):
            log_work_from_workflows(JIRA_USER, JIRA_PASSWORD, JIRA_SERVER, command_two)
    elif(command_one == "log"):
        try:
            command_two = getArgument(2, '')
            command_three = getArgument(3, '')
            command_four = getArgument(4, '')
            log_work_from_cli(JIRA_USER, JIRA_PASSWORD, JIRA_SERVER, command_three, command_four)
        except Exception as error:
            failure(error)






