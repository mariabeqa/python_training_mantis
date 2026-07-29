from model.project import Project


def test_add_project(app, soap, gen_project):
    new_project = gen_project
    old_projects = soap.get_all_projects()
    app.project.add(new_project)
    new_projects = soap.get_all_projects()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(new_project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)