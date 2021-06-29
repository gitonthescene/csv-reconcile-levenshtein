from nox_poetry import session, SDIST

args = lambda s: s.split()


@session
def test_main(session):
    session.poetry.installroot(distribution_format=SDIST)
    session.install('pytest')
    session.install('csv-reconcile')
    session.run(*args('pytest -v'))
