import json
import requests


class DatabaseClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.pattern = "http://{}:{}/{}".format(self.ip, self.port, "{}")

    def send(self, query, data):
        try:
            resp = requests.post(url=self.pattern.format(query),
                                 data=data)
        except Exception:
            print("access db failed")
        else:
            res = resp.json()
            return res

    def get_list(self, oj, number=10):
        data = {'number': number,
                'oj': oj}
        res = self.send("get_list", data)
        return res["problem_list"]

    def save_list(self, lst):
        data = {'lst': json.dumps(lst)}
        res = self.send("save_list", data)
        return True

    def get_problem(self, oj, problemid):
        data = {'oj': oj,
                'problemid': problemid}
        #print("{} {}:{}".format("oj", oj, type(oj)))
        #print("{} {}:{}".format("problemid", problemid, type(problemid)))
        res = self.send("get_problem", data)
        return res['problem']

    def save_problem(self, problem):
        data = {'problem': json.dumps(problem)}
        #print("{} {}:{}".format("problem", problem, type(problem)))
        res = self.send("save_problem", data)
        return True

    def get_title(self, oj, problemid):
        data = {'oj': oj,
                'problemid': problemid}
        #print("{} {}:{}".format("oj", oj, type(oj)))
        #print("{} {}:{}".format("problemid", problemid, type(problemid)))
        res = self.send("get_title", data)
        return res['title']

    def reset(self):
        data = {}
        res = self.send("reset", data)
        return True

