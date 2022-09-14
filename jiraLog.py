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
    jira = JIRA(
        basic_auth=(username, password),
        server=server
    )
    myself = jira.myself()


def failure(error):
    print("Command Incorrect")
    print(error)

def helpCommand():
    print(f'./jiraLog.py log <hours/minutes: 6h or 6m> <ticket number>')
    print(f' ./jiraLog.py workflow <workflow name here>')
    print("pray because I did not write a help command")

def log_work_from_workflows(username, password, server, workflow):
    jira = JIRA(
        basic_auth=(username, password),
        server=server
    )
    myself = jira.myself()
    for x in workflows[workflow]:
        print(x)
        jira.add_worklog(issue=x['issue'], timeSpent=x['length'])

def log_work_from_cli(username, password, server, length, ticket):
    jira = JIRA(
        basic_auth=(username, password),
        server=server
    )
    myself = jira.myself()
    jira.add_worklog(issue=ticket, timeSpent=length)


def getArgument(position, default_value):
    if(len(sys.argv) > position):
        return sys.argv[position]
    else:
        return default_value


workflows = {
    'OOO': [{
        'issue': 'SOFT-9',
        'length': '8h',
        'startTime': '8:00'
    }],
    'normalWorkDay': [{
        'issue': 'SOFT-6',
        'length': '1h',
        'startTime': '10:00'
    },{
        'issue': 'SOFT-6',
        'length': '5h',
        'startTime': '10:00'
    }],
    'newWorkFlow': [{
        'issue': 'SOFT-6',
        'length': '1h',
        'startTime': '10:00'
    },{
        'issue': 'SOFT-6',
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
            command_one = getArgument(1, '')
            command_two = getArgument(2, '')
            command_three = getArgument(3, '')
            log_work_from_cli(JIRA_USER, JIRA_PASSWORD, JIRA_SERVER, command_two, command_three)
        except Exception as error:
            failure(error)
    else:
        helpCommand()






