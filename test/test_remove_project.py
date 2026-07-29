import random

from model.project import Project


def test_remove_project(app, soap, gen_project):
    if len(soap.get_all_projects()) == 0:
        app.project.add(gen_project)
    old_projects = soap.get_all_projects()
    project_to_delete = random.choice(old_projects)
    app.project.delete_project_by_id(project_to_delete.id)
    new_projects = soap.get_all_projects()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project_to_delete)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
