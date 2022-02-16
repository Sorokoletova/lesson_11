import json


def get_candidates_list():
    """ Получаем всех кандидатов"""

    with open("candidates.json", encoding='utf8') as file:
        candidates_list = json.load(file)

    return candidates_list


def get_candidates_by_id(number_id):
    """Получаем кандидатов по id
    number_id - id кандидата в файле"""

    candidates = get_candidates_list()
    for candidate in candidates:
        if candidate["id"] == number_id:
            return candidate


def get_candidates_skill(skill):
    """Получаем кандидата по skill"""

    candidates = get_candidates_list()
    candidates_skill = []
    skill_l = skill.lower()
    for candidate in candidates:
        candidates_list = candidate["skills"].lower().split(", ")
        if skill_l in candidates_list:
            candidates_skill.append(candidate)

    return candidates_skill


def get_candidates_by_name(candidate_name):
    """Получаем кандидата по имени"""

    candidates = get_candidates_list()
    candidates_list = []
    name = candidate_name.lower()
    for candidate in candidates:
        if name in candidate["name"].lower():
            candidates_list.append(candidate)
    return candidates_list
