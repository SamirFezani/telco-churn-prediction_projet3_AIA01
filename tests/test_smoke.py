
def test_import_package():
    import importlib
    importlib.import_module('src.telco_churn')
    assert True
