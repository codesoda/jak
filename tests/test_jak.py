import pytest
from click.testing import CliRunner
from jak.app import main as jak


@pytest.fixture
def runner():
    return CliRunner()


def test_empty(runner):
    result = runner.invoke(jak)
    assert result.exit_code == 0
    assert not result.exception


@pytest.mark.parametrize('version_flag', [
        '--version',
        '-v']
    )
def test_version(runner, version_flag):
    result = runner.invoke(jak, [version_flag])
    expected_output = 'Jak v0.1.0 (Troubled Toddler)'
    assert not result.exception
    assert result.exit_code == 0
    assert result.output.strip() == expected_output


def test_encrypt_smoke(runner):
    result = runner.invoke(jak, ['encrypt', 'secret', '--password', 'password'])
    assert result.output == 'zqnVrSb-Q3bFxN9jOdzZBw==\n'


def test_decrypt_smoke(runner):
    result = runner.invoke(jak, ['decrypt', 'zqnVrSb-Q3bFxN9jOdzZBw==', '--password', 'password'])
    assert result.output == 'secret\n'