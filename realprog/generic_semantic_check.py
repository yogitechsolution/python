import re
import sys
from pprint import pprint
import requests
import os
import json
import typing
from html.parser import HTMLParser

class ResponseHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self._lines = []
    
    @property
    def lines(self) -> typing.List[str]:
        return self._lines

    def handle_starttag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        self._lines.append(data)
        

class ConventionalMrResponse:
    def __init__(self):
        pass

    ok = False
    is_draft = False
    has_type = False
    has_issue = False
    has_extra = False
    has_half = False
    has_resthalf = False

    def to_dict(self):
        return {
            "ok": self.ok,
            "draft": self.is_draft,
            "type": self.has_type,
            "issue": self.has_issue,
            "extra": self.has_extra,
            "half": self.has_half,
            "resthalf": self.has_resthalf
        }

class ConventionalMr:
    def __init__(self):
        pass

    _draft = str("^((Draft|WIP): )")
    _type = "(feat|fix|chore|refactor|perf|style|test|docs|ci|revert):"
    _message = "(.+)"
    _issue = "((\(((CAV)\-\d+|HOTFIX|COMPAT)\))+)"
    _extra = "(\((HIDE|API CHANGE)\))"
    _full = "{}?{} {} {}\s*{}?$".format(_draft, _type, _message, _issue, _extra)
    _half = "{}?{} {}{}{}?$".format(_draft, _type, _message, _issue, _extra)
    _resthalf = "{}?{}{} {}{}?$".format(_draft, _type, _message, _issue, _extra)
    _message = ""

    def check(self, message):
        self._message = message
        res = ConventionalMrResponse()
        res.ok = self._is_all_ok()
        res.is_draft = self._is_draft()
        res.has_type = self._has_correct_type()
        res.has_issue = self._has_issue()
        res.has_extra = self._has_extra()
        res.has_half = self._has_half()
        res.has_resthalf = self._has_resthalf()
        return res

    def _is_all_ok(self):
        pattern = re.compile(self._full)
        if pattern.match(self._message):
            return True
        return False

    def _is_draft(self):
        pattern = re.compile(self._draft)
        result = pattern.findall(self._message)
        return len(result) > 0

    def _has_correct_type(self):
        pattern = re.compile("{}?{}".format(self._draft, self._type))
        if pattern.match(self._message):
            return True
        return False

    def _has_issue(self):
        pattern = re.compile(self._issue)
        result = pattern.findall(self._message)
        return len(result) > 0

    def _has_extra(self):
        pattern = re.compile(self._extra)
        result = pattern.findall(self._message)
        return len(result) > 0

    def _has_half(self):
        pattern = re.compile(self._half)
        if pattern.match(self._message):
            return True
        return False

    def _has_resthalf(self):
        pattern = re.compile(self._resthalf)
        if pattern.match(self._message):
            return True
        return False

def usage():
    print("TODO: Add usage")

if __name__ == "__main__":
    if len(sys.argv) == 4:
        title_string = sys.argv[1]
        ci_merge_request_project_id = sys.argv[2]
        ci_merge_request_iid = sys.argv[3]
        ci_server_host = os.environ.get("CI_SERVER_HOST")
        gitlab_push_key = os.environ.get("GITLAB_PUSH_KEY")
        json_data = "<h1>Please use a semantic merge request title</h1><br>"
        json_data_type = """
        <b>Please use the allowed types: chore, docs, feat, fix, perf, refactor, style, ci, test or revert</b><br>
        <b>Types described:<br>
        <b>feat - A new feature<br>\n<b>fix - A bug fix<br>\n<b>docs - Documentation only changes<br>
        <b>style - Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)<br>
        <b>refactor - A code change that neither fixes a bug nor adds a feature<br>
        <b>perf - A code change that improves performance<br>
        <b>test - Adding missing tests or correcting existing tests<br>
        <b>ci - Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)<br>
        <b>chore - Other changes that don't modify src or test files<br>
        <b>revert - Reverts a previous commit<br>
        """
        json_data_example = "<b>Example-feat: Added semantic check .pre job for MR title (CAV-xxxxx)</b><br>"
        response = ConventionalMr().check(title_string)
        if not response.ok:
            #Check if there are required spaces in the MR title
            if (not response.has_half or  not response.has_resthalf) and (response.has_type and response.has_issue):
                json_data = "{}<b>Give mandatory spaces after the type and before the issue in the MR title </b><br>{}".format(json_data,json_data_example)
            #check for type
            if not response.has_type:
                type_pattern =  r'feat|fix|perf|style|ci|revert|refactor|chore|docs|test' 
                type_pattern_with_colon = r'feat:|fix:|perf:|style:|ci:|revert:|refactor:|chore:|docs:|test:'
                match_type = re.match(type_pattern, title_string, re.IGNORECASE)
                match_type_with_colon = re.match(type_pattern_with_colon, title_string, re.IGNORECASE)
                #Check for allowed type
                if match_type:
                    matched_type = match_type.group()
                    #Check for lowercase of type
                    if matched_type.islower():
                        #Check for type followed by colon
                        if match_type_with_colon:
                            matched_type_with_colon = match_type_with_colon.group()
                        else:
                            json_data = "{} The type should be followed by colon".format(json_data)
                    else:
                        if match_type_with_colon:
                            matched_type_with_colon = match_type_with_colon.group()
                            json_data = "{}<b>The given type contains uppercase, all letters in type should be of lowercase.</b><br>".format(json_data)
                        else:
                            json_data = "{}<b>The given type contains uppercase, all letters in type should be of lowercase.</b><br>".format(json_data)
                            json_data = "{} And the type should be followed by colon".format(json_data)
                else:
                    json_data= "{}<b>The given type does not match the allowed types or the type for MR is missing</b><br>{}".format(json_data,json_data_type)   
            if not response.has_issue:
                # Check for issue
                issue_pattern =  r'CAV-\d+|HOTFIX|API CHANGE' 
                match_issue = re.search(issue_pattern, title_string, re.IGNORECASE)
                if match_issue:
                    matched_issue = match_issue.group(0)
                    # Check if issue is uppercase
                    if matched_issue.isupper():
                        json_data="{}<b>Found Issue but it should be enclosed in braces in this format: (CAV-xxxx)</b><br>".format(json_data)
                    else:
                        json_data="{}<b>Found Issue but it should be in UPPERCASE and enclosed in braces in this format: (CAV-xxxx)</b><br>".format(json_data)
                 # Check for issue with colon
                issue_pattern_with_colon = r'CAV:\d+'
                match_issue_with_colon = re.search(issue_pattern_with_colon, title_string, re.IGNORECASE)
                if match_issue_with_colon:
                    matched_issue_with_colon = match_issue_with_colon.group(0)
                    if matched_issue_with_colon.isupper():
                        json_data="{}<b>Found Issue with colon it should be enclosed in braces in this format: (CAV-xxxx)</b><br>".format(json_data)
                    else:
                        json_data="{}<b>Found Issue but it should be in UPPERCASE enclosed in braces like this: (CAV-xxxx)</b><br>".format(json_data)
                if not match_issue and not match_issue_with_colon:
                    json_data= "{}<b>Missing Issue: CAV-XXXX, HOTFIX, API CHANGE (Mandatory UPPERCASE and Can be multiple)</b><br>".format(json_data)
            headers = {"Content-Type": "application/json","PRIVATE-TOKEN": gitlab_push_key}
            data = {"body": json_data}
            url = "https://{}/api/v4/projects/{}/merge_requests/{}/discussions".format(ci_server_host,ci_merge_request_project_id,ci_merge_request_iid)
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                print("Request was successful!")
                json_obj = json.loads(response.text)
                
                for note in json_obj['notes']:
                    print("Action needs to be taken:")
                    html_parser = ResponseHTMLParser()
                    html_parser.feed(note['body'])
                    for line in html_parser.lines:
                        print(f"- {line}")
            else:
                print("Request failed with status code:", response.status_code)
            exit(1)
        exit(0)
