from flask import Flask
import utils

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = utils.load_candidates()
    list_of_candidates = ""

    for candidate in candidates:
        list_of_candidates += f"{candidate['name']}\n"
        list_of_candidates += f"{candidate['position']}\n"
        list_of_candidates += f"{candidate['skills']}\n"
        list_of_candidates += f"\n"

    return "<pre>" + list_of_candidates + "</pre>"


@app.route("/candidates/<int:id>")
def page_candidate_by_id(id):
    candidate = utils.get_candidate_by_id(id)
    info_of_candidate = ""

    info_of_candidate += f"<img src=\"{candidate['picture']}\">\n"
    info_of_candidate += f"{candidate['name']}\n"
    info_of_candidate += f"{candidate['position']}\n"
    info_of_candidate += f"{candidate['skills']}\n"

    return "<pre>" + info_of_candidate + "</pre>"


@app.route("/skills/<skill>")
def page_candidates_by_skills(skill):
    skilled_candidates = utils.candidate_by_skills(skill)
    list_of_candidates = ""

    for candidate in skilled_candidates:
        list_of_candidates += f"{candidate['name']}\n"
        list_of_candidates += f"{candidate['position']}\n"
        list_of_candidates += f"{candidate['skills']}\n"
        list_of_candidates += f"\n"

    return "<pre>" + list_of_candidates + "</pre>"
app.run()
