import os
import requests

IGNORE_TITLE = "Information Center"
token = os.getenv('DTOKEN')
key = os.getenv('KEY')
# issue classes
Reported = "Reported"
Investigating = "Investigating"
In_Progress = "In Progress"
Fix_Ready = "Fix Ready"
Fix_Live = "Fix Live"


class Issue:
    def __init__(self, issues_class, title, description, labels):
        self.issues_class = issues_class
        self.title = title
        self.description = description
        self.labels = labels

    def __str__(self):
        lab = "["
        for _l in self.labels:
            lab += _l + ", "
        lab += "]"
        return "**Title** : " + self.title + "\n" + "**Description** : " + \
               self.description + "\n" + "**Label** : " + lab + "\n\n"


class Div2KnownIssues:
    def __init__(self):
        self.reported = []
        self.investigating = []
        self.in_progress = []
        self.fix_ready = []
        self.fix_live = []

    def add_issue(self, issue):
        if issue.issues_class == Reported:
            self.reported.append(issue)
        elif issue.issues_class == Investigating:
            self.investigating.append(issue)
        elif issue.issues_class == In_Progress:
            self.in_progress.append(issue)
        elif issue.issues_class == Fix_Ready:
            self.fix_ready.append(issue)
        elif issue.issues_class == Fix_Live:
            self.fix_live.append(issue)
        else:
            raise Exception("Invalid issue class")


def get_data():
    # issue holder
    issue_data = Div2KnownIssues()

    # ge list
    url = "https://api.trello.com/1/lists/"
    # todo : read from env file
    query = {
        'key': key,
        'token': token
    }

    # get list ids
    url_ = 'https://trello.com/b/F2RU9ia9/the-division-2-known-issues.json'
    r = requests.get(url_)
    r_ = r.json()

    ids = set()
    for c in r_['cards']:
        ids.add(c['idList'])

    # get lists names
    list_names = {}
    for id_ in ids:
        # print(id_)
        _url = url + id_

        response = requests.request(
            "GET",
            _url,
            params=query
        )

        rj = response.json()
        list_names[str(id_)] = rj['name']

    # create data as json

    _data = {}
    current_title = ""

    for c in r_['cards']:
        _title = list_names[str(c['idList'])]
        if _title != IGNORE_TITLE:
            if current_title != _title:
                current_title = _title
            _data['title'] = current_title
            _data['name'] = c["name"]
            _data['desc'] = c["desc"]
            labels = c["labels"]
            # only list issues with label
            # currently all issues comes with a label
            # is changed check this
            if labels:
                # print(lables)
                _l = []
                for label in labels:
                    _l.append(label["name"])
                issue_ = Issue(current_title, _data['name'], _data['desc'], _l)
                issue_data.add_issue(issue_)
            _data.clear()

    # json_data = json.dumps(data)

    return issue_data
