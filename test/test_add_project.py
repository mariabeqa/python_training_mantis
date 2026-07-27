from model.project import Project


def test_add_project(app, db, gen_project):
    new_project = gen_project
    old_projects = db.get_project_list()
    app.project.add(new_project)
    new_projects = db.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(new_project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)