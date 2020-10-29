from fixture.application import Application
import pytest

@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.open_home_page()
    fixture.session.login(name='admin', password='secret')
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
