from model.group import Group
import pytest

def test_group_list(app,db):
    with pytest.allure.step('Get UI group list'):
        ui_list=app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    with pytest.allure.step('Get DB group list'):
        db_list=map(clean,db.get_group_list())
    with pytest.allure.step('Check the UI list is equal to the DB list'):
        assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

