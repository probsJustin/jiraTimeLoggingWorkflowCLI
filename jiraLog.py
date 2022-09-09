from collections import Counter
from typing import cast

from jira import JIRA
from jira.client import ResultList
from jira.resources import Issue
import sys

JIRA_SERVER = ''
JIRA_USER = ''
JIRA_PASSWORD = ''

def log_work_from_workflows( username, password, server, workflow):
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
    for x in workflows[workflow]:
        print(x)
        jira.add_worklog(issue=x['issue'], timeSpent=x['length'])

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
    }]
}

print(workflows['OOO'])

command_one = getArgument(1, 'help')
if(command_one):
    if(command_one == "workflow"):
        command_two = getArgument(2, '')
        if(command_two != '' and command_two in workflows.keys()):
            log_work_from_workflows(JIRA_USER, JIRA_PASSWORD, JIRA_SERVER, command_two)
    else:
        print("I honestly dont have much help here")





